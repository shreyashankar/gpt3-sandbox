"""Idea taken from https://www.notion.so/Sentence-Email-Generator-a36d269ce8e94cc58daf723f8ba8fe3e"""

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from api import GPT, Example, UIConfig
from api import demo_web_app
from csv import reader
from pathlib import Path


# Construct GPT object and show some examples
gpt = GPT(engine="ada",
          temperature=0.2,
          max_tokens=25)

with open('examples/emails.csv', 'r') as email_dataset:
    email_files = reader(email_dataset)

    for row in email_files:
        email_file = row[0]
        expected_subject = row[1]
        expected_body = Path('data/'+email_file).read_text()
        expected_body = expected_body.replace('\n', '')

        gpt.add_example(Example(expected_body, expected_subject))

# Define UI configuration
config = UIConfig(description="Email body to Subject generator",
                  button_text="Generate",
                  placeholder="Ask RAM Co. if they have new storage units in stock.")

demo_web_app(gpt, config)
