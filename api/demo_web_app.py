from flask import Flask, request, jsonify
from flask_cors import CORS
import openai

def submit_openai_request(prime_text, prompt):
    query = prime_text + "input: " + prompt + "\n"
    response = openai.Completion.create(engine="davinci",
                                        prompt=query,
                                        max_tokens=100,
                                        temperature=0.5,
                                        top_p=1,
                                        n=1,
                                        stream=False,
                                        stop="\ninput:") 
    return response
    

def demo_web_app(gpt, config):
    prime_text = gpt.get_prime_text()
    app = Flask(__name__)
    app.config.from_envvar('LATEX_TRANSLATOR_CONFIG')
    CORS(app)
    openai.api_key = app.config['OPENAI_KEY']

    @app.route("/params", methods=['GET'])
    def get_params():
        response = config.to_dict()
        return response

    @app.route("/translate", methods=['GET', 'POST'])
    def translate():
        prompt = request.json['prompt']
        response = submit_openai_request(prime_text, prompt)
        return {'text': response['choices'][0]['text'][7:]}

    app.run()
