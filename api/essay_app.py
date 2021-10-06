"""Runs the web app given a GPT object and UI configuration."""

from http import HTTPStatus
import json
import subprocess
import openai

from flask import Flask, request, Response, send_from_directory

from .gpt import set_openai_key, Example
from .ui_config import UIConfig
import os, sys
from api import GPT, Example, UIConfig, GPT3_FineTuned
from api.essay_airtable import insert_record

CONFIG_VAR = "OPENAI_CONFIG"
KEY_NAME = "OPENAI_KEY"
MODEL_NAME = "MODEL"


def essay_app(gpt, config=UIConfig()):
    global app
    
    """Creates Flask app to serve the React app."""
    try:
        app.config.from_envvar(CONFIG_VAR)
        set_openai_key(app.config[KEY_NAME])
    except (FileNotFoundError,RuntimeError) as e:
        set_openai_key(str(os.environ.get('OPENAI_KEY')))

    @app.route("/params", methods=["GET"])
    def get_params():
        # pylint: disable=unused-variable
        response = config.json()
        return response

    def error(err_msg, status_code):
        return Response(json.dumps({"error": err_msg}), status=status_code)

    def get_example(example_id):
        """Gets a single example or all the examples."""
        # return all examples
        if not example_id:
            return json.dumps(gpt.get_all_examples())

        example = gpt.get_example(example_id)
        if not example:
            return error("id not found", HTTPStatus.NOT_FOUND)
        return json.dumps(example.as_dict())

    def post_example():
        """Adds an empty example."""
        new_example = Example("", "")
        gpt.add_example(new_example)
        return json.dumps(gpt.get_all_examples())

    def put_example(args, example_id):
        """Modifies an existing example."""
        if not example_id:
            return error("id required", HTTPStatus.BAD_REQUEST)

        example = gpt.get_example(example_id)
        if not example:
            return error("id not found", HTTPStatus.NOT_FOUND)

        if "input" in args:
            example.input = args["input"]
        if "output" in args:
            example.output = args["output"]

        # update the example
        gpt.add_example(example)
        return json.dumps(example.as_dict())

    def delete_example(example_id):
        """Deletes an example."""
        if not example_id:
            return error("id required", HTTPStatus.BAD_REQUEST)

        gpt.delete_example(example_id)
        return json.dumps(gpt.get_all_examples())

    @app.route(
        "/examples",
        methods=["GET", "POST"],
        defaults={"example_id": ""},
    )
    @app.route(
        "/examples/<example_id>",
        methods=["GET", "PUT", "DELETE"],
    )
    def examples(example_id):
        method = request.method
        args = request.json
        if method == "GET":
            return get_example(example_id)
        if method == "POST":
            return post_example()
        if method == "PUT":
            return put_example(args, example_id)
        if method == "DELETE":
            return delete_example(example_id)
        return error("Not implemented", HTTPStatus.NOT_IMPLEMENTED)

    @app.route("/translate", methods=["GET", "POST"])
    def translate():
        # pylint: disable=unused-variable
        prompt = request.json["prompt"]
        response = gpt.submit_request(prompt)
        offset = 0
        if not gpt.append_output_prefix_to_query:
            offset = len(gpt.output_prefix)

        response = {'text': response['choices'][0]['text'][offset:]}
        print(f'Response received:{response}')
        return response

    @app.route('/')
    def serve():
        return send_from_directory(app.static_folder, 'index.html')

    @app.route("/record", methods=["POST"])
    def record():
        body = request.json
        vals = body.values()
        print(f'body teehee: {body}')
        response = insert_record(vals)
        return response

app = Flask(__name__,
    static_folder='../build',static_url_path='')

demo = False
model = "curie:ft-user-mkdwhtbbymt0rzgay0sqg9d4-2021-10-04-12-15-36"
gpt = GPT3_FineTuned(model=model, max_tokens=1, append_output_prefix_to_query=True)

config = UIConfig(description= "Write your essay here",
                button_text= "Grade my Essay!",
                placeholder= "This popular story is about a hare (an animal belonging to the rabbit family), which is known to move quickly and a tortoise, which is known to move slower.The story began when the hare who has won many races proposed a race with the tortoise. The hare simply wanted to prove that he was the best and have the satisfaction of beating him.The tortoise agreed and the race began.The hare got a head-start but became overconfident towards the end of the race. His ego made him believe that he could win the race even if he rested for a while.And so, he took a nap right near the finish line.Meanwhile, the tortoise walked slowly but extremely determined and dedicated. He did not give up for a second and kept persevering despite the odds not being in his favour.While the hare was asleep, the tortoise crossed the finish line and won the race!The best part was that the tortoise did not gloat or put the hare down!")

essay_app(gpt, config=config)

if __name__ == "__main__":
    app.run(host='0.0.0.0')

