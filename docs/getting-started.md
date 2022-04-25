# Getting Started

## Creating a GPT-3 Powered Web App

Note: This is a work in progress, but the essential functions are described here.

First, you will want to create a `GPT` object, which optionally acceps the parameters `engine`, `temperature`, and `max_tokens` (otherwise defaults to values in the following snippet):

```
from api import GPT

gpt = GPT(engine="davinci",
          temperature=0.5,
          max_tokens=100)
```

Since we're mainly interested in constructing a demo, we do not provide an interface for you to change other parameters. Feel free to fork the repository and make as many changes to the code as you would like.

Once the `GPT` object is created, you need to "prime" it with several examples. The goal of these examples are to show the model some patterns that you are hoping for it to recognize. The `Example` constructor accepts an input string and a corresponding output string. To construct an `Example`, you can run the following code:

```
from api import Example

ex = Example(inp="Hello", out="Hola")
```

After constructing some examples, you can add them to your `GPT` object by calling the `add_example` method, which only accepts an `Example`:

```
gpt.add_example(ex)
```

Finally, once you've added all of your examples, it's time to run the demo! But first, in order to customize the web app to your idea, you can optionally create a `UIConfig` with `description`, `button_text`, and `placeholder` (text initially shown in the input box) parameters:

```
from api import UIConfig

config = UIConfig(description="Analogies generator",
                  button_text="Generate",
                  placeholder="Memes are like")
```

Now you can run the web app! Call the `demo_web_app` with your `GPT` and (optional) `UIConfig` objects:

```
from api import demo_web_app

demo_web_app(gpt, config)
```

Save this python script to a file and run the file as you would normally run a Python file:

`python path_to_file.py`

in your shell. A web app should pop up in your browser in a few seconds, and you should be able to interact with your primed model. Please open any issues if you have questions!
