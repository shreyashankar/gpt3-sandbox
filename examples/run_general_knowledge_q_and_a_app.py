"""An example of changing the default "input:"/"output:" query structure \
to a "Q:"/"A:" structure, and of appending the prompt query with "A: " """

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from api import GPT, Example, TextFormat, QueryFormat, UIConfig
from api import demo_web_app

QUESTION_PREFIX = 'Q: '
QUESTION_SUFFIX = '\n'
ANSWER_PREFIX = 'A: '
ANSWER_SUFFIX = '\n\n'
APPEND_OUTPUT_PREFIX_TO_QUERY = True

query_format = QueryFormat(
    TextFormat(QUESTION_PREFIX, QUESTION_SUFFIX),
    TextFormat(ANSWER_PREFIX, ANSWER_SUFFIX),
    APPEND_OUTPUT_PREFIX_TO_QUERY)


# Construct GPT object and show some examples
gpt = GPT(engine="davinci",
          temperature=0.5,
          max_tokens=100,
          query_format=query_format)

gpt.add_example(Example('What is human life expectancy in the United States?', \
 'Human life expectancy in the United States is 78 years.'))
gpt.add_example(
    Example('Who was president of the United States in 1955?', \
    'Dwight D. Eisenhower was president of the United States in 1955.'))
gpt.add_example(Example(
    'What party did he belong to?', \
    'He belonged to the Republican Party.'))
gpt.add_example(Example('Who was president of the United States before George W. Bush?', \
'Bill Clinton was president of the United States before George W. Bush.'))
gpt.add_example(Example('In what year was the Coronation of Queen Elizabeth?', \
'The Coronation of Queen Elizabeth was in 1953.'))


# Define UI configuration
config = UIConfig(description="Question to Answer",
                  button_text="Answer",
                  placeholder="Who wrote the song 'Hey Jude'?")

demo_web_app(gpt, config)
