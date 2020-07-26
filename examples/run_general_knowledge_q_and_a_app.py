import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from api import demo_web_app
from api import GPT, Example, UIConfig


question_prefix = 'Q: '
question_suffix = "\n"
answer_prefix = "A: "
answer_suffix = "\n\n"


# Construct GPT object and show some examples
gpt = GPT(engine="davinci",
          temperature=0.5,
          max_tokens=100,
          input_prefix=question_prefix,
          input_suffix=question_suffix,
          output_prefix=answer_prefix,
          output_suffix=answer_suffix,
          append_output_prefix_to_query=True)

gpt.add_example(Example('What is human life expectancy in the United States?',
                        'Human life expectancy in the United States is 78 years.'))
gpt.add_example(
    Example('Who was president of the United States in 1955?', 'Dwight D. Eisenhower was president of the United States in 1955.'))
gpt.add_example(Example(
    'What party did he belong to?', 'He belonged to the Republican Party.'))
gpt.add_example(Example('Who was president of the United States before George W. Bush?',
                        'Bill Clinton was president of the United States before George W. Bush.'))
gpt.add_example(Example('In what year was the Coronation of Queen Elizabeth?',
                        'The Coronation of Queen Elizabeth was in 1953.'))


# Define UI configuration
config = UIConfig(description="Question to Answer",
                  button_text="Answer",
                  placeholder="Who wrote the song 'Hey Jude'?")

demo_web_app(gpt, config)
