"""Runs the web app given a GPT object and UI configuration."""

import subprocess
import openai

from flask import Flask, request

from .gpt import set_openai_key, Example
from .ui_config import UIConfig

CONFIG_VAR = "OPENAI_CONFIG"
KEY_NAME = "OPENAI_KEY"


def demo_web_app(gpt, config=UIConfig()):
    """Creates Flask app to serve the React app."""
    app = Flask(__name__)

    app.config.from_envvar(CONFIG_VAR)
    set_openai_key(app.config[KEY_NAME])

    @app.route("/params", methods=["GET"])
    def get_params():
        # pylint: disable=unused-variable
        response = config.json()
        return response

    @app.route("/translate", methods=["GET", "POST"])
    def translate():
        # pylint: disable=unused-variable
        req_json = request.json
        prompt = req_json["prompt"]
        if config.show_example_form and len(req_json["examples"]) > 0:
            for ex in req_json["examples"]:
                gpt.add_example(Example(ex["input"], ex["output"]))
        response = gpt.submit_request(prompt)
        return {"text": response["choices"][0]["text"][7:]}

    subprocess.Popen(["yarn", "start"])
    app.run()
