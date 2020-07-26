"""Creates the Example and GPT classes for a user to interface with the OpenAI API."""

import openai
import uuid


def set_openai_key(key):
    """Sets OpenAI key."""
    openai.api_key = key


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

    def format(self):
        """Formats the input, output pair."""
        return f"input: {self.input}\noutput: {self.output}\n"


class GPT:
    """The main class for a user to interface with the OpenAI API.
    A user can add examples and set parameters of the API request."""

    def __init__(self, engine="davinci", temperature=0.5, max_tokens=100):
        self.examples = {}
        self.engine = engine
        self.temperature = temperature
        self.max_tokens = max_tokens

    def add_example(self, ex):
        """Adds an example to the object. Example must be an instance
        of the Example class."""
        assert isinstance(ex, Example), "Please create an Example object."
        self.examples[ex.get_id()] = ex

    def clear_example(self, id):
        """Clears example with the specific id"""
        if id in self.examples:
            del self.examples[id]

    def get_example(self, id):
        """ Get a single example """
        return self.examples.get(id, None)

    def get_all_examples(self):
        """ Returns all examples as a list of dicts"""
        return {k: v.as_dict() for k, v in self.examples.items()}

    def get_prime_text(self):
        """Formats all examples to prime the model."""
        return "\n".join([i.format() for i in self.examples.values()]) + "\n"

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
        return self.get_prime_text() + "input: " + prompt + "\n"

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
            stop="\ninput:",
        )
        return response

    def get_top_reply(self, prompt):
        """Obtains the best result as returned by the API."""
        response = self.submit_request(prompt)
        return response["choices"][0]["text"]
