"""Creates the Example and GPT classes for a user to interface with the OpenAI
API."""
import os
import torch
from huggingface_hub import snapshot_download
from accelerate import (
    init_empty_weights,
    dispatch_model,
    infer_auto_device_map,
    load_checkpoint_and_dispatch,
)
from transformers import (
    AutoConfig,
    AutoModelForCausalLM,
    AutoTokenizer,
    AutoModelForSeq2SeqLM,
)
from api.lm import LanguageModel


class OPT(LanguageModel):
    """The main class for a user to interface with the OpenAI API.

    A user can add examples and set parameters of the API request.
    """

    def __init__(
        self,
        engine="125m",
        temperature=0.5,
        max_tokens=100,
        input_prefix="input: ",
        input_suffix="\n",
        output_prefix="output: ",
        output_suffix="\n\n",
        append_output_prefix_to_query=False,
    ):
        self.examples = {}
        self.engine = engine
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.input_prefix = input_prefix
        self.input_suffix = input_suffix
        self.output_prefix = output_prefix
        self.output_suffix = output_suffix
        self.append_output_prefix_to_query = append_output_prefix_to_query
        self.stop = (output_suffix + input_prefix).strip()
        self.model = self.create_engine()

    def create_engine(self):
        checkpoint = f"facebook/opt-{self.engine}"
        weights_path = snapshot_download(checkpoint)

        # If the folder contains a checkpoint that isn't sharded, it needs to point to the state dict directly
        # otherwise point to the directory containing the shard
        files = os.listdir(weights_path)
        weights_path = (
            os.path.join(weights_path, "pytorch_model.bin")
            if "pytorch_model.bin" in files
            else weights_path
        )
        config = AutoConfig.from_pretrained(checkpoint)
        if torch.cuda.is_available():
            # Initializes an empty shell with the model. This is instant and does not take any RAM.
            with init_empty_weights():
                model = AutoModelForCausalLM.from_config(config)
            # Initialize the model under the previous context manager breaks the tied weights.
            model.tie_weights()

            # Infer device map automatically
            device_map = infer_auto_device_map(
                model.model,
                no_split_module_classes=["OPTDecoderLayer"],
                dtype="float16",
            )

            if any([k == "disk" for k in device_map.values()]):
                offload_folder = "offload_folder"
            else:
                offload_folder = None

            if "30b" in checkpoint:
                # Set a few layers to use the disk manually to ensure enough RAM for the 30B checkpoint.
                device_map["decoder.layers.23"] = "disk"
                device_map["decoder.layers.24"] = "disk"
                device_map["decoder.layers.25"] = "disk"
                device_map["decoder.layers.26"] = "disk"
                device_map["decoder.layers.27"] = "disk"

            self.device_map = device_map
            load_checkpoint_and_dispatch(
                model.model,
                weights_path,
                device_map=device_map,
                offload_folder=offload_folder,
                dtype="float16",
                offload_state_dict=True,
            )
            model.tie_weights()
        else:
            model = AutoModelForCausalLM.from_config(config)

        self.tokenizer = AutoTokenizer.from_pretrained(f"facebook/opt-{self.engine}")
        return model

    def submit_request(self, prompt):
        """Generates using the opt model."""
        prompt = self.craft_query(prompt)

        inputs = self.tokenizer(prompt, return_tensors="pt")
        response = self.model.generate(
            inputs["input_ids"],
            # inputs["input_ids"].to(0),
            max_length=self.get_max_tokens(),
            temperature=self.get_temperature(),
            top_p=1,
        )
        return self.tokenizer.decode(response[0].tolist())

    def get_top_reply(self, prompt):
        """Obtains the best result as returned by the API."""
        response = self.submit_request(prompt)
        return response["choices"][0]["text"]
