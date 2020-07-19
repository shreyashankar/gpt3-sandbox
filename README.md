# GPT-3 Priming Tool

Authors: shreyashankar, bora-uyumazturk
Initial release date: 19 July 2020

## Description

This project includes backend and web tools to make it simple to experiment and create a web app demo with the OpenAI GPT-3 API. You can locally launch a web app to demo your GPT-3 idea by writing a simple Python script.

The backend is in Flask, and the frontend is in React.

## Requirements

* API keys from the OpenAI API beta invite
* Python 3
* `yarn`

Instructions to install Python 3 are [here](https://realpython.com/installing-python/), and instructions to install `yarn` are [here](https://classic.yarnpkg.com/en/docs/install/#mac-stable).

## Setup

To set up your virtual environment, do the following:

1. Create a virtual environment in the root directory: `python -m venv $ENV_NAME`
2. Activate the virtual environment: ` source $ENV_NAME/bin/activate`
3. Install requirements: `pip install -r requirements.txt`
4. To add your secret key: create a file anywhere on your computer called `openai.cfg` with the contents `OPENAI_KEY=$YOUR_SECRET_KEY`, where `$YOUR_SECRET_KEY` looks something like `sk-somerandomcharacters`. If you are unsure what your secret key is, navigate to the [API docs](https://beta.openai.com/developer-quickstart) and copy the token displayed next to the "secret" key type.
5. Set your environment variable to read the secret key: run `export OPENAI_CONFIG=/path/to/config/openai.cfg`

To verify that your environment is set up properly, navigate to one of the scripts in the `examples` directory. Run one of them:

`python run_latex_app.py`

A new tab should pop up in your browser, and you should be able to interact with the UI! To stop this app, run ctrl-c or command-c in your terminal.

## Quickstart


