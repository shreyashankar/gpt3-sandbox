# GPT-3 Sandbox: Turn your ideas into demos in a matter of minutes

Initial release date: 19 July 2020

Note that this repository is not under any active development; just basic maintenance.

## Description

The goal of this project is to enable users to create cool web demos using the newly released OpenAI GPT-3 API **with just a few lines of Python.** 

This project addresses the following issues:

1. Automatically formatting a user's inputs and outputs so that the model can effectively pattern-match
2. Creating a web app for a user to deploy locally and showcase their idea

Here's a quick example of priming GPT to convert English to LaTeX:

```
# Construct GPT object and show some examples
gpt = GPT(engine="davinci",
          temperature=0.5,
          max_tokens=100)
gpt.add_example(Example('Two plus two equals four', '2 + 2 = 4'))
gpt.add_example(Example('The integral from zero to infinity', '\\int_0^{\\infty}'))
gpt.add_example(Example('The gradient of x squared plus two times x with respect to x', '\\nabla_x x^2 + 2x'))
gpt.add_example(Example('The log of two times x', '\\log{2x}'))
gpt.add_example(Example('x squared plus y squared plus equals z squared', 'x^2 + y^2 = z^2'))

# Define UI configuration
config = UIConfig(description="Text to equation",
                  button_text="Translate",
                  placeholder="x squared plus 2 times x")

demo_web_app(gpt, config)
```

Running this code as a python script would automatically launch a web app for you to test new inputs and outputs with. There are already 3 example scripts in the `examples` directory.

You can also prime GPT from the UI. for that, pass `show_example_form=True` to `UIConfig` along with other parameters.

Technical details: the backend is in Flask, and the frontend is in React. Note that this repository is currently not intended for production use.

## Background

GPT-3 ([Brown et al.](https://arxiv.org/abs/2005.14165)) is OpenAI's latest language model. It incrementally builds on model architectures designed in [previous](https://arxiv.org/abs/1706.03762) [research](https://arxiv.org/abs/1810.04805) studies, but its key advance is that it's extremely good at "few-shot" learning. There's a [lot](https://twitter.com/sharifshameem/status/1282676454690451457) [it](https://twitter.com/jsngr/status/1284511080715362304?s=20) [can](https://twitter.com/paraschopra/status/1284801028676653060?s=20) [do](https://www.gwern.net/GPT-3), but one of the biggest pain points is in "priming," or seeding, the model with some inputs such that the model can intelligently create new outputs. Many people have ideas for GPT-3 but struggle to make them work, since priming is a new paradigm of machine learning. Additionally, it takes a nontrivial amount of web development to spin up a demo to showcase a cool idea. We built this project to make our own idea generation easier to experiment with.

This [developer toolkit](https://www.notion.so/API-Developer-Toolkit-49595ed6ffcd413e93ebff10d7e70fe7) has some great resources for those experimenting with the API, including sample prompts.

## Requirements

Coding-wise, you only need Python. But for the app to run, you will need:

* API key from the OpenAI API beta invite
* Python 3
* `yarn`
* Node 16

Instructions to install Python 3 are [here](https://realpython.com/installing-python/), instructions to install `yarn` are [here](https://classic.yarnpkg.com/en/docs/install/#mac-stable) and we recommend using nvm to install (and manage) Node (instructions are [here](https://github.com/nvm-sh/nvm)).

## Setup

First, clone or fork this repository. Then to set up your virtual environment, do the following:

1. Create a virtual environment in the root directory: `python -m venv $ENV_NAME`
2. Activate the virtual environment: ` source $ENV_NAME/bin/activate` (for MacOS, Unix, or Linux users) or ` .\ENV_NAME\Scripts\activate` (for Windows users)
3. Install requirements: `pip install -r api/requirements.txt`
4. To add your secret key: create a file anywhere on your computer called `openai.cfg` with the contents `OPENAI_KEY=$YOUR_SECRET_KEY`, where `$YOUR_SECRET_KEY` looks something like `'sk-somerandomcharacters'` (including quotes). If you are unsure what your secret key is, navigate to the [API Keys page](https://beta.openai.com/account/api-keys) and click "Copy" next to a token displayed under "Secret Key". If there is none, click on "Create new secret key" and then copy it.
5. Set your environment variable to read the secret key: run `export OPENAI_CONFIG=/path/to/config/openai.cfg` (for MacOS, Unix, or Linux users) or `set OPENAI_CONFIG=/path/to/config/openai.cfg` (for Windows users)
6. Run `yarn install` in the root directory

If you are a Windows user, to run the demos, you will need to modify the following line inside `api/demo_web_app.py`:
`subprocess.Popen(["yarn", "start"])` to `subprocess.Popen(["yarn", "start"], shell=True)`.

To verify that your environment is set up properly, run one of the 3 scripts in the `examples` directory:
`python examples/run_latex_app.py`.

A new tab should pop up in your browser, and you should be able to interact with the UI! To stop this app, run ctrl-c or command-c in your terminal.

To create your own example, check out the ["getting started" docs](https://github.com/shreyashankar/gpt3-sandbox/blob/master/docs/getting-started.md).

## Interactive Priming

The real power of GPT-3 is in its ability to learn to specialize to tasks given a few examples. However, priming can at times be more of an art than a science. Using the GPT and Example classes, you can easily experiment with different priming examples and immediately see their GPT on GPT-3's performance. Below is an example showing it improve incrementally at translating English to LaTeX as we feed it more examples in the python interpreter: 

```
>>> from api import GPT, Example, set_openai_key
>>> gpt = GPT()
>>> set_openai_key(key)
>>> prompt = "integral from a to b of f of x"
>>> print(gpt.get_top_reply(prompt))
output: integral from a to be of f of x

>>> gpt.add_example(Example("Two plus two equals four", "2 + 2 = 4"))
>>> print(gpt.get_top_reply(prompt))
output:

>>> gpt.add_example(Example('The integral from zero to infinity', '\\int_0^{\\infty}'))
>>> print(gpt.get_top_reply(prompt))
output: \int_a^b f(x) dx

``` 

## Contributions

We actively encourage people to contribute by adding their own examples or even adding functionalities to the modules. Please make a pull request if you would like to add something, or create an issue if you have a question. We will update the contributors list on a regular basis.

Please *do not* leave your secret key in plaintext in your pull request!

## Authors

The following authors have committed 20 lines or more (ordered according to the Github contributors page):

* Shreya Shankar
* Bora Uyumazturk
* Devin Stein
* Gulan
* Michael Lavelle


