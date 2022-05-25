"""Creates the Example and GPT classes for a user to interface with the OpenAI
API."""

import openai
from api.lm import LanguageModel


def set_openai_key(key):
    """Sets OpenAI key."""
    openai.api_key = key


class GPT(LanguageModel):
    """The main class for a user to interface with the OpenAI API.

    A user can add examples and set parameters of the API request.
    """

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
