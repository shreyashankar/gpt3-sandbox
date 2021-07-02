import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from api import GPT, Example, UIConfig
from api import demo_web_app

gpt = GPT(temperature=0.5, max_tokens=500)

gpt.add_example(Example(
    "A boy named John was upset. His father found him crying.When his father asked John why he was crying, he said that he had a lot of problems in his life.His father simply smiled and asked him to get a potato, an egg, and some coffee beans. He placed them in three bowls.He then asked John to feel their texture and then fill each bowl with water.John did as he had been told. His father then boiled all three bowls.Once the bowls had cooled down, John’s father asked him to feel the texture of the different food items again.John noticed that the potato had become soft and its skin was peeling off easily; the egg had become harder and tougher; the coffee beans had completely changed and filled the bowl of water with aroma and flavour.",
    "Life will always have problems and pressures, like the boiling water in the story. It’s how you respond and react to these problems that counts the most!"
))

gpt.add_example(Example(
    "Once upon a time in a circus, five elephants that performed circus tricks. They were kept tied up with weak rope that they could’ve easily escaped, but did not.One day, a man visiting the circus asked the ringmaster: “Why haven’t these elephants broken the rope and run away?”The ringmaster replied: “From when they were young, the elephants were made to believe that they were not strong enough to break the ropes and escape.”It was because of this belief that they did not even try to break the ropes now.",
    "Don’t give in to the limitations of society. Believe that you can achieve everything you want to!"
))

gpt.add_example(Example(
    "A long time ago, there lived a king in Greece named Midas.He was extremely wealthy and had all the gold he could ever need. He also had a daughter whom he loved very much.One day, Midas saw a Satyr (an angel) who was stuck and was in trouble. Midas helped the Satyr and asked for his wish to be granted in return.The Satyr agreed and Midas wished for everything he touched to be turned to gold. His wish was granted.Extremely excited, Midas went home to his wife and daughter touching pebbles, rocks, and plants on the way, which turned into gold.As his daughter hugged him, she turned into a golden statue.Having learnt his lesson, Midas begged the Satyr to reverse the spell who granted that everything would go back to their original state.",
    "Stay content and grateful with what you have. Greed will not get you anywhere."
))




config = UIConfig(description= "Describe the moral of the short story",
                  button_text= "Get Moral",
                  placeholder= "This popular story is about a hare (an animal belonging to the rabbit family), which is known to move quickly and a tortoise, which is known to move slower.The story began when the hare who has won many races proposed a race with the tortoise. The hare simply wanted to prove that he was the best and have the satisfaction of beating him.The tortoise agreed and the race began.The hare got a head-start but became overconfident towards the end of the race. His ego made him believe that he could win the race even if he rested for a while.And so, he took a nap right near the finish line.Meanwhile, the tortoise walked slowly but extremely determined and dedicated. He did not give up for a second and kept persevering despite the odds not being in his favour.While the hare was asleep, the tortoise crossed the finish line and won the race!The best part was that the tortoise did not gloat or put the hare down!")

demo_web_app(gpt, config)
