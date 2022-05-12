"""Creates the Example and GPT classes for a user to interface with the OpenAI
API."""

import openai


class GPT:
    """The main class for a user to interface with the OpenAI API.

    A user can add examples and set parameters of the API request.
    """

    def __init__(
        self,
        engine="davinci",
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

    def submit_request(self, prompt):
        """Calls the OpenAI API with the specified parameters."""
        response = openai.Completion.create(
            engine=self.get_engine(),
            prompt=self.craft_query(prompt),
            max_tokens=self.get_max_tokens(),
            temperature=self.get_temperature(),
            top_p=1,
            n=1,
            stream=False,
            stop=self.stop,
        )
        return response

    def get_top_reply(self, prompt):
        """Obtains the best result as returned by the API."""
        response = self.submit_request(prompt)
        return response["choices"][0]["text"]