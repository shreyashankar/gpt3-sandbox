from flask import Flask, request, jsonify
from flask_cors import CORS
import openai

class GPT:

    def __init__(self):
        self.prime_text = "English: Two plus two equals four\nLaTeX: 2 + 2 = 4\n\nEnglish: The integral from zero to infinity\nLaTeX: \\int_0^{\\infty}\n\nEnglish: The gradient of x squared plus two times x with respect to x\nLaTeX: \\nabla_x x^2 + 2x\n\nEnglish: The log of two times x\nLaTeX: \\log{2x}\n\nEnglish: x squared plus y squared plus equals z squared\nLaTeX: x^2 + y^2 = z^2\n\nEnglish: The sum from zero to twelve of i squared\nLaTeX: \\sum_{i=0}^{12} i^2\n\nEnglish: E equals m times c squared\nLaTeX: E = mc^2\n\nEnglish: H naught of t\nLaTeX: H_0(t)\n\nEnglish: f of n equals 1 over (b-a) if n is 0 otherwise 5\nLaTeX: f(n) = \\begin{cases} 1/(b-a) &\\mbox{if } n \\equiv 0 \\\
    5 \\end{cases}\n\n"
    
    def demo_web_app(self):
        app = Flask(__name__)
        app.config.from_envvar('LATEX_TRANSLATOR_CONFIG')
        CORS(app)

        @app.route("/translate", methods=['GET', 'POST'])
        def translate():
            prompt = request.json['prompt']
            openai.api_key = app.config['OPENAI_KEY'] 
            query = self.prime_text + "English: " + prompt + "\n"
            response = openai.Completion.create(engine="davinci",
                                                prompt=query,
                                                max_tokens=100,
                                                temperature=0.5,
                                                top_p=1,
                                                n=1,
                                                stream=False,
                                                stop="\nEnglish:")
            return {'text':response['choices'][0]['text']}
        
        app.run()

gpt = GPT()
gpt.demo_web_app()
