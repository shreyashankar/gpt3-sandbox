"""Idea taken from https://www.notion.so/Sentence-Email-Generator-a36d269ce8e94cc58daf723f8ba8fe3e"""

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from api import GPT, Example, UIConfig
from api import demo_web_app


# Construct GPT object and show some examples
gpt = GPT(engine="davinci",
          temperature=0.4,
          max_tokens=60)

gpt.add_example(Example('Thank John for the book.',
                        'Dear John, Thank you so much for the book. I really appreciate it. I hope to hang out soon. Your friend, Sarah.'))

gpt.add_example(Example('Tell TechCorp I appreciate the great service.',
                        'To Whom it May Concern, I want you to know that I appreciate the great service at TechCorp. The staff is outstanding and I enjoy every visit. Sincerely, Bill Johnson'))

gpt.add_example(Example('Invoice Kelly Watkins $500 for design consultation.',
                        'Dear Ms. Watkins, This is my invoice for $500 for design consultation. It was a pleasure to work with you. Sincerely, Emily Fields'))

gpt.add_example(Example('Invite Amanda and Paul to the company event Friday night.',
                        'Dear Amanda and Paul, I hope this finds you doing well. I want to invite you to our company event on Friday night. It will be a great opportunity for networking and there will be food and drinks. Should be fun. Best, Ryan'))

# Define UI configuration
config = UIConfig(description="Command to email generator",
                  button_text="Generate",
                  placeholder="Ask RAM Co. if they have new storage units in stock.")

demo_web_app(gpt, config)
