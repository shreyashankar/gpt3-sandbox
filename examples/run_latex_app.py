import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from api import GPT, Example, UIConfig
from api import demo_web_app


# Construct GPT object and show some examples
gpt = GPT(engine="davinci",
          temperature=0.5,
          max_tokens=100)

gpt.add_example(Example('Two plus two equals four', '2 + 2 = 4'))
gpt.add_example(
    Example('The integral from zero to infinity', '\\int_0^{\\infty}'))
gpt.add_example(Example(
    'The gradient of x squared plus two times x with respect to x', '\\nabla_x x^2 + 2x'))
gpt.add_example(Example('The log of two times x', '\\log{2x}'))
gpt.add_example(
    Example('x squared plus y squared plus equals z squared', 'x^2 + y^2 = z^2'))
gpt.add_example(
    Example('The sum from zero to twelve of i squared', '\\sum_{i=0}^{12} i^2'))
gpt.add_example(Example('E equals m times c squared', 'E = mc^2'))
gpt.add_example(Example('H naught of t', 'H_0(t)'))
gpt.add_example(Example('f of n equals 1 over (b-a) if n is 0 otherwise 5',
                        'f(n) = \\begin{cases} 1/(b-a) &\\mbox{if } n \\equiv 0 \\\ # 5 \\end{cases}'))

# Define UI configuration
config = UIConfig(description="Text to equation",
                  button_text="Translate",
                  placeholder="x squared plus 2 times x")

demo_web_app(gpt, config)
