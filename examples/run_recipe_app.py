import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from api import GPT, Example, UIConfig
from api import demo_web_app

gpt = GPT(temperature=0.5, max_tokens=500)

gpt.add_example(Example(
    "how to roast eggplant",
    "How do you cook eggplant in the oven? Well, there are a couple ways. To roast whole eggplants in the oven, leave the skin on and roast at 400 degrees F (200 degrees C) until the skin gets wrinkly and begins to collapse in on the softened fruit. This method will also produce velvety smooth eggplant dips or spreads."
))

gpt.add_example(Example(
    "how to bake eggplant",
    "To bake eggplant, you'll cut the eggplant into rounds or strips and prepare them as the recipe indicates -- for example, you can dredge them in egg and breadcrumbs or simply brush them with olive oil and bake them in a 350 degree F oven."
))

gpt.add_example(Example(
    "how to make puerto rican steamed rice",
    "Bring vegetable oil, water, and salt to a boil in a saucepan over high heat. Add rice, and cook until the water has just about cooked out; stir. Reduce heat to medium-low. Cover, and cook for 20 to 25 minutes. Stir again, and serve. Rice may be a little sticky and may stick to bottom of pot."
))

gpt.add_example(Example(
    "how to make oatmeal peanut butter cookies",
    "Preheat oven to 350 degrees F (175 degrees C). In a large bowl, cream together shortening, margarine, brown sugar, white sugar, and peanut butter until smooth. Beat in the eggs one at a time until well blended. Combine the flour, baking soda, and salt; stir into the creamed mixture. Mix in the oats until just combined. Drop by teaspoonfuls onto ungreased cookie sheets. Bake for 10 to 15 minutes in the preheated oven, or until just light brown. Don't over-bake. Cool and store in an airtight container."
))


config = UIConfig(description= "How to cook stuff",
                  button_text= "show me",
                  placeholder= "how to make a breakfast burrito")

demo_web_app(gpt, config)
