import subprocess

from flask import Flask, request, jsonify
from flask_cors import CORS
import openai

from .UIConfig import UIConfig

def demo_web_app(gpt, config=UIConfig()):
    app = Flask(__name__)
    app.config.from_envvar('LATEX_TRANSLATOR_CONFIG')
    CORS(app)
    gpt.set_openai_key(app.config['OPENAI_KEY'])

    @app.route("/params", methods=['GET'])
    def get_params():
        response = config.json()
        return response

    @app.route("/translate", methods=['GET', 'POST'])
    def translate():
        prompt = request.json['prompt']
        response = gpt.submit_request(prompt) 
        return {'text': response['choices'][0]['text'][7:]}

    subprocess.Popen(["yarn", "start"])
    app.run()
