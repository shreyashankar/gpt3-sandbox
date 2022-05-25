"""Creates the Example and GPT classes for a user to interface with the OpenAI
API."""

import uuid


class Example:
    """Stores an input, output pair and formats it to prime the model."""

    def __init__(self, inp, out):
        self.input = inp
        self.output = out
        self.id = uuid.uuid4().hex

    def get_input(self):
        """Returns the input of the example."""
        return self.input

    def get_output(self):
        """Returns the intended output of the example."""
        return self.output

    def get_id(self):
        """Returns the unique ID of the example."""
        return self.id

    def as_dict(self):
        return {
            "input": self.get_input(),
            "output": self.get_output(),
            "id": self.get_id(),
        }


class LanguageModel:
    """The main class for a user to interface with the OpenAI API or a Huggingface language model (LM).

    A user can add examples and set parameters of the API request/LM inference.
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
        preamble="",
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
        self.preamble = preamble
        self.append_output_prefix_to_query = append_output_prefix_to_query
        self.stop = (output_suffix + input_prefix).strip()

    def add_example(self, ex):
        """Adds an example to the object.

        Example must be an instance of the Example class.
        """
        assert isinstance(ex, Example), "Please create an Example object."
        self.examples[ex.get_id()] = ex

    def delete_example(self, id):
        """Delete example with the specific id."""
        if id in self.examples:
            del self.examples[id]

    def get_example(self, id):
        """Get a single example."""
        return self.examples.get(id, None)

    def get_all_examples(self):
        """Returns all examples as a list of dicts."""
        return {k: v.as_dict() for k, v in self.examples.items()}

    def get_prime_text(self):
        """Formats all examples to prime the model."""
        return "".join([self.format_example(ex) for ex in self.examples.values()])

    def get_engine(self):
        """Returns the engine specified for the API."""
        return self.engine

    def get_temperature(self):
        """Returns the temperature specified for the API."""
        return self.temperature

    def get_max_tokens(self):
        """Returns the max tokens specified for the API."""
        return self.max_tokens

    def craft_query(self, prompt):
        """Creates the query for the API request."""
        q = (
            self.preamble
            + self.get_prime_text()
            + self.input_prefix
            + prompt
            + self.input_suffix
        )
        if self.append_output_prefix_to_query:
            q = q + self.output_prefix

        return q

    def submit_request(self, prompt):
        """Calls the LanguageModel API with the specified parameters."""
        pass

    def get_top_reply(self, prompt):
        """Obtains the best result as returned by the API."""
        pass

    def format_example(self, ex):
        """Formats the input, output pair."""
        return (
            self.input_prefix
            + ex.get_input()
            + self.input_suffix
            + self.output_prefix
            + ex.get_output()
            + self.output_suffix
        )
