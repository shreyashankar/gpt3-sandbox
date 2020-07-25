"""Runs the web app given a GPT object and UI configuration."""

import json
import subprocess
import openai

from flask import Flask, request, Response

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

    def error(err_msg, status_code):
        return Response(json.dumps({"error": err_msg}), status=status_code)

    @app.route(
        "/examples", methods=["GET", "POST"], defaults={"example_id": ""},
    )
    @app.route(
        "/examples/<example_id>", methods=["GET", "PUT", "DELETE"],
    )
    def examples(example_id):
        method = request.method
        args = request.json
        if method == "GET":
            # gets either a single example or all of them.
            if example_id:
                example = gpt.get_example(example_id)
                if example:
                    return json.dumps(example.as_dict())
                return error("id not found", 404)
            return json.dumps(gpt.get_all_examples())
        elif method == "POST":
            # adds an empty example.
            new_example = Example("", "")
            gpt.add_example(new_example)
            return json.dumps(gpt.get_all_examples())
        elif method == "PUT":
            # modifies an existing example.
            if example_id:
                example = gpt.get_example(example_id)
                if example:
                    if args.get("input", None):
                        example.input = args["input"]
                    if args.get("output", None):
                        example.output = args["output"]
                    return json.dumps(example.as_dict())
                return error("id not found", 404)
            return error("id required", 400)
        elif method == "DELETE":
            # deletes an example.
            if example_id:
                gpt.clear_example(example_id)
                return json.dumps(gpt.get_all_examples())
            return error("id required", 400)
        return error("Not implemented", 501)

    @app.route("/translate", methods=["GET", "POST"])
    def translate():
        # pylint: disable=unused-variable
        prompt = request.json["prompt"]
        response = gpt.submit_request(prompt)
        return {"text": response["choices"][0]["text"][7:]}

    subprocess.Popen(["yarn", "start"])
    app.run()
