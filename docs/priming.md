## Priming

As smart as GPT-3 is, it still doesn't excel at most tasks out of the box. It
benefits greatly from seeing a few examples, a process we like to refer to as "priming".
Finding a set of examples which focuses GPT-3 on your specific use case will inevitably require 
a bit of trial-and-error. To make this step easier, we designed our GPT interface to allow for 
easy testing and exploration using the python interactive interpreter. Below we walk you through 
an example of how to do so, again using the English to LaTeX use case. 

First, open up your python interpreter by running `python` or `python3`. Next you'll need to 
import the necessary items from the `api` package. You'll need the `GPT` class,
the `Example` class, and `set_openai_key`:

```
>>> from api import GPT, Example, set_openai_key
``` 

Next, you'll want to set your open ai key to gain access to the beta. 

```
>>> set_openai_key("YOUR_OPENAI_KEY") # omit the Bearer, it should look like "sk-..."
```

Next, initialize your GPT class. You have the option of setting a few of the query
parameters such as `engine` and `temperature`, but we'll just go with the default
setup for simplicity.

```
>>> gpt = GPT()
```

Now we're ready to give it a prompt and see how it does! You can conveniently get
GPT-3's response using the `get_top_reply` method.

```
>>> print(gpt.get_top_reply("sum from one to infinity of one over n squared"))

output: n squared over n

```

Clearly this needs some priming. To prime, you call `add_example` on your `gpt` object,
feeding it an instance of the `Example` class.  Let's add a few examples and try again.

```
>>> gpt.add_example(Example("four y plus three x cubed", "4y + 3x^3"))
>>> gpt.add_example(Example("integral from a to b", "\\int_a^b"))
>>> print(gpt.get_top_reply("sum from one to infinity of one over n squared"))
output: 1/n^2

```

Better, but not quite there. Better, but not quite there. Let's give it an expression with a 
sum and then see what happens: 

```
>>> gpt.add_example(Example("sum from zero to twelve of i", "\\sum_{i=0}^5 i"))
>>> print(gpt.get_top_reply("sum from one to infinity of one over n squared"))
output: \sum_{n=1}^\infty \frac{1}{n^2}

>>> print(gpt.get_top_reply("sum from one to infinity of one over two to the n"))
output: \sum_{n=1}^\infty \frac{1}{2^n}
```

Finally, it works! Now go and see what other crazy stuff you can do with GPT-3!





