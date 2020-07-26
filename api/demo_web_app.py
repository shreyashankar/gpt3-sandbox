"""Runs the web app given a GPT object and UI configuration."""

import subprocess
import openai

from flask import Flask, request

from .gpt import set_openai_key
from .ui_config import UIConfig

CONFIG_VAR = "OPENAI_CONFIG"
KEY_NAME = "OPENAI_KEY"

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
        offset = 0
        if not gpt.get_append_output_prefix_to_query():
            offset = len(gpt.query_format.output_format.prefix)
        return {'text': response['choices'][0]['text'][offset:]}

    subprocess.Popen(["yarn", "start"])
    app.run()
