import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from api import GPT, Example, UIConfig
from api import demo_web_app


# Construct GPT object and show some examples
gpt = GPT(engine="davinci", temperature=0.5, max_tokens=100)

gpt.add_example(Example("Who are you?", "I'm an example."))
gpt.add_example(Example("What are you?", "I'm an example."))

# Define UI configuration
config = UIConfig(
    description="Prompt",
    button_text="Result",
    placeholder="Where are you?",
    show_example_form=True,
)

demo_web_app(gpt, config)
