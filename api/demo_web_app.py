"""Runs the web app given a GPT object and UI configuration."""

import subprocess
import openai

from flask import Flask, request

from .ui_config import UIConfig

CONFIG_VAR = "OPENAI_CONFIG"
KEY_NAME = "OPENAI_KEY"

def set_openai_key(key):
    """Sets OpenAI key."""
    openai.api_key = key

def demo_web_app(gpt, config=UIConfig()):
    """Creates Flask app to serve the React app."""
    app = Flask(__name__)

    app.config.from_envvar(CONFIG_VAR)
    set_openai_key(app.config[KEY_NAME])

    @app.route("/params", methods=['GET'])
    def get_params():
        # pylint: disable=unused-variable
        response = config.json()
        return response

    @app.route("/translate", methods=['GET', 'POST'])
    def translate():
        # pylint: disable=unused-variable
        prompt = request.json['prompt']
        response = gpt.submit_request(prompt)
        return {'text': response['choices'][0]['text'][7:]}

    subprocess.Popen(["yarn", "start"])
    app.run()
