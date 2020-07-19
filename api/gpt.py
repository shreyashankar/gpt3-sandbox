from flask import Flask, request, jsonify
from flask_cors import CORS
import openai

class Example():
    def __init__(self, inp, out):
        self.input = inp
        self.output = out
    
    def format(self):
        return f"input: {self.input}\noutput: {self.output}\n"

class GPT:

    def __init__(self):
        self.examples = []

    def add_example(self, ex):
        assert isinstance(ex, Example), "Please create an Example object."
        self.examples.append(ex.format())
    
    def demo_web_app(self):
        prime_text = '\n'.join(self.examples) + '\n'

        app = Flask(__name__)
        app.config.from_envvar('LATEX_TRANSLATOR_CONFIG')
        CORS(app)

        @app.route("/translate", methods=['GET', 'POST'])
        def translate():
            prompt = request.json['prompt']
            openai.api_key = app.config['OPENAI_KEY'] 
            query = prime_text + "input: " + prompt + "\n"
            response = openai.Completion.create(engine="davinci",
                                                prompt=query,
                                                max_tokens=100,
                                                temperature=0.5,
                                                top_p=1,
                                                n=1,
                                                stream=False,
                                                stop="\ninput:")                                 
            return {'text':response['choices'][0]['text'][7:]}
        
        app.run()

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
gpt.demo_web_app()