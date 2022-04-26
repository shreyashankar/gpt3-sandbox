import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from api import GPT, Example, UIConfig
from api import demo_web_app


# Construct GPT object and show some examples
gpt = GPT(engine="davinci", temperature=0.5, max_tokens=100)

gpt.add_example(Example("Ads for shoes", "Shoes so comfortable you want to walk in them."))
gpt.add_example(Example("Ads for barber", "Hairs so slick you can stare into a mirror all day."))
gpt.add_example(Example("Ads for fries", "Fries so good you can't handle it."))
gpt.add_example(Example("Ads for sunglasses", "Sun glasses so cool you would wear them indoor."))
gpt.add_example(Example("Ads for theme park", "Rides so fun you could enjoy it with your boss."))
gpt.add_example(Example("Ads for politician", "Country so corruption-free you would make Singapore jealous."))

# Define UI configuration
config = UIConfig(
    description="Ad Slogan Generator",
    button_text="Create Slogan",
    placeholder="Ads for hats",
    show_example_form=False,
)

demo_web_app(gpt, config)
