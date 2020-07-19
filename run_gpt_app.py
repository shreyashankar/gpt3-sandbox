from api.demo_web_app import demo_web_app
from api.GPT import GPT, Example
from api.UIConfig import UIConfig

# prime GPT
gpt = GPT()
gpt.add_example(Example('Two plus two equals four', '2 + 2 = 4'))
gpt.add_example(Example('The integral from zero to infinity', '\\int_0^{\\infty}'))
gpt.add_example(Example('The gradient of x squared plus two times x with respect to x', '\\nabla_x x^2 + 2x'))
gpt.add_example(Example('The log of two times x', '\\log{2x}'))
gpt.add_example(Example('x squared plus y squared plus equals z squared', 'x^2 + y^2 = z^2'))
gpt.add_example(Example('The sum from zero to twelve of i squared', '\\sum_{i=0}^{12} i^2'))
gpt.add_example(Example('E equals m times c squared', 'E = mc^2'))
gpt.add_example(Example('H naught of t', 'H_0(t)'))
gpt.add_example(Example('f of n equals 1 over (b-a) if n is 0 otherwise 5', 'f(n) = \\begin{cases} 1/(b-a) &\\mbox{if } n \\equiv 0 \\\ # 5 \\end{cases}'))

# define configuration
config = UIConfig(description="My GPT App",
                  buttonText="Run GPT",
                  placeholder="How are you this morning, GPT?")

demo_web_app(gpt, config)
