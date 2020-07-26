"""Creates the Example and GPT classes for a user to interface with the OpenAI API."""

import openai


def set_openai_key(key):
    """Sets OpenAI key."""
    openai.api_key = key

class Example():
    """Stores an input, output pair it to prime the model."""

    def __init__(self, inp, out):
        self.input = inp
        self.output = out

    def get_input(self):
        """Returns the input of the example."""
        return self.input

    def get_output(self):
        """Returns the intended output of the example."""
        return self.output

class TextFormat():
    """Formats text by prefixing and suffixing with the provided parameters."""

    def __init__(self, prefix, suffix):
        self.prefix = prefix
        self.suffix = suffix

    def get_prefix(self):
        """Returns the prefix of this format."""
        return self.prefix

    def get_suffix(self):
        """Returns the suffix of this format."""
        return self.suffix

    def get_wrapped_text(self, text):
        """Formats the input, output pair."""
        return self.prefix + text + self.suffix

class QueryFormat():
    """Formats a query."""

    def __init__(self, input_format=TextFormat("input: ", "\n"),
                 output_format=TextFormat("output: ", "\n\n"),
                 append_output_prefix_to_query=False):
        self.input_format = input_format
        self.output_format = output_format
        self.append_output_prefix_to_query = append_output_prefix_to_query

    def get_input_format(self):
        """Returns the example input format."""
        return self.input_format

    def get_output_format(self):
        """Returns the example output format."""
        return self.output_format

    def get_append_output_prefix_to_query(self):
        """Indicates whether the output prefix should be appended to the query."""
        return self.append_output_prefix_to_query

    def format_example(self, ex):
        """Formats the input, output pair."""
        return self.input_format.get_wrapped_text(ex.get_input()) \
        + self.output_format.get_wrapped_text(ex.get_output())

    def get_stop_token(self):
        """Returns the stop token of this query format."""
        return (self.output_format.get_suffix() \
        + self.input_format.get_prefix()).strip()


    def format_query(self, prime_text, prompt):
        """Creates the query for the API request."""
        query = prime_text + self.input_format.get_wrapped_text(prompt)
        if self.append_output_prefix_to_query:
            query = query + self.output_format.get_prefix()
        return query

class GPT:
    """The main class for a user to interface with the OpenAI API.
    A user can add examples and set parameters of the API request."""

    def __init__(self, engine='davinci',
                 temperature=0.5,
                 max_tokens=100,
                 query_format=QueryFormat()):
        self.examples = []
        self.engine = engine
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.query_format = query_format

    def add_example(self, ex):
        """Adds an example to the object. Example must be an instance
        of the Example class."""
        assert isinstance(ex, Example), "Please create an Example object."
        self.examples.append(self.query_format.format_example(ex))

    def get_prime_text(self):
        """Formats all examples to prime the model."""
        return ''.join(self.examples)

    def get_engine(self):
        """Returns the engine specified for the API."""
        return self.engine

    def get_temperature(self):
        """Returns the temperature specified for the API."""
        return self.temperature

    def get_max_tokens(self):
        """Returns the max tokens specified for the API."""
        return self.max_tokens

    def get_append_output_prefix_to_query(self):
        """Returns the suffix of this format."""
        return self.query_format.get_append_output_prefix_to_query()

    def craft_query(self, prompt):
        """Creates the query for the API request."""
        return self.query_format.format_query(self.get_prime_text(), prompt)

    def submit_request(self, prompt):
        """Calls the OpenAI API with the specified parameters."""
        response = openai.Completion.create(engine=self.get_engine(),
                                            prompt=self.craft_query(prompt),
                                            max_tokens=self.get_max_tokens(),
                                            temperature=self.get_temperature(),
                                            top_p=1,
                                            n=1,
                                            stream=False,
                                            stop=self.query_format.get_stop_token())
        return response

    def get_top_reply(self, prompt):
        """Obtains the best result as returned by the API."""
        response = self.submit_request(prompt)
        return response['choices'][0]['text']
