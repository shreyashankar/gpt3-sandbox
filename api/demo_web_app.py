from flask import Flask, request, jsonify
from flask_cors import CORS
import openai

from .UIConfig import UIConfig

CONFIG_VAR = "OPENAI_CONFIG"
KEY_NAME = "OPENAI_KEY"

def submit_openai_request(gpt, prompt):
    response = openai.Completion.create(engine=gpt.get_engine(),
                                        prompt=gpt.craft_query(prompt),
                                        max_tokens=gpt.get_max_tokens(),
                                        temperature=gpt.get_temperature(),
                                        top_p=1,
                                        n=1,
                                        stream=False,
                                        stop="\ninput:") 
    return response
    

def demo_web_app(gpt, config=UIConfig()):
    app = Flask(__name__)
    app.config.from_envvar(CONFIG_VAR)
    CORS(app)
    openai.api_key = app.config[KEY_NAME]

    @app.route("/params", methods=['GET'])
    def get_params():
        response = config.json()
        return response

    @app.route("/translate", methods=['GET', 'POST'])
    def translate():
        prompt = request.json['prompt']
        response = submit_openai_request(gpt, prompt)
        return {'text': response['choices'][0]['text'][7:]}

    app.run()
