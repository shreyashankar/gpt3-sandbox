import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from api import GPT, Example, UIConfig
from api import demo_web_app

PROMPT_EXAMPLE_URL = "https://raw.githubusercontent.com/ml4j/gpt-scrolls/master/tweets/twitter-fiction-prompt.json"
TEMPLATE_EXAMPLE_URL = "https://raw.githubusercontent.com/ml4j/gtp-3-prompt-templates/master/question-answer/default/templates/question_answer_template_2.json"

import requests
import json

prompt_example_json = json.loads(requests.get(PROMPT_EXAMPLE_URL).text)
template_json = json.loads(requests.get(TEMPLATE_EXAMPLE_URL).text)

# Construct GPT object and show some examples
gpt = GPT(engine="davinci",
          temperature=1.1,
          max_tokens=100,
          input_prefix=template_json['questionPrefix'],
          input_suffix=template_json['questionSuffix'],
          output_prefix=template_json['answerPrefix'],
          output_suffix=template_json['answerSuffix'],
          append_output_prefix_to_query=False,
          premise_prefix=template_json['premisePrefix'],
          premise_suffix=template_json['premiseSuffix'])

gpt.set_premise(prompt_example_json['premise'])

for example in prompt_example_json['questionsAndAnswers']:
    gpt.add_example(Example(example['question'], example['answer']))

# Define UI configuration
config = UIConfig(description="Twitter Fiction",
                  button_text="Generate",
                  placeholder=prompt_example_json['defaultPromptQuestion'])


demo_web_app(gpt, config)
