import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from api import GPT, Example, UIConfig, GPT3_FineTuned
from api import demo_web_app
from api.essay_app import essay_app 

demo = False
model = "curie:ft-user-mkdwhtbbymt0rzgay0sqg9d4-2021-10-04-12-15-36"
gpt = GPT3_FineTuned(model=model, max_tokens=1, append_output_prefix_to_query=True)

config = UIConfig(description= "Write your essay here",
                  button_text= "Grade my Essay!",
                  placeholder= "This popular story is about a hare (an animal belonging to the rabbit family), which is known to move quickly and a tortoise, which is known to move slower.The story began when the hare who has won many races proposed a race with the tortoise. The hare simply wanted to prove that he was the best and have the satisfaction of beating him.The tortoise agreed and the race began.The hare got a head-start but became overconfident towards the end of the race. His ego made him believe that he could win the race even if he rested for a while.And so, he took a nap right near the finish line.Meanwhile, the tortoise walked slowly but extremely determined and dedicated. He did not give up for a second and kept persevering despite the odds not being in his favour.While the hare was asleep, the tortoise crossed the finish line and won the race!The best part was that the tortoise did not gloat or put the hare down!")

if demo:
    demo_web_app(gpt, config)
else:
    app = essay_app(gpt,config)
    app.run()
