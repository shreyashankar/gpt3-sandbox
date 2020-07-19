from flask import Flask, request, jsonify
from flask_cors import CORS
import openai

from .UIConfig import UIConfig

CONFIG_VAR = "OPENAI_CONFIG"
KEY_NAME = "OPENAI_KEY"

def demo_web_app(gpt, config=UIConfig()):
    app = Flask(__name__)
    CORS(app)

    app.config.from_envvar(CONFIG_VAR)
    gpt.set_openai_key(app.config[KEY_NAME])

    @app.route("/params", methods=['GET'])
    def get_params():
        response = config.json()
        return response

    @app.route("/translate", methods=['GET', 'POST'])
    def translate():
        prompt = request.json['prompt']
        response = gpt.submit_request(prompt) 
        return {'text': response['choices'][0]['text'][7:]}

    app.run()
