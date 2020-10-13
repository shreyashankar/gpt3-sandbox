import numpy as np
import os
import pandas as pd

from api import GPT, Example, set_openai_key
from multiprocessing import Pool
from sklearn.model_selection import ParameterGrid

"""
We will be controlling the following parameters:

- temperature
- top P
- frequency penalty
- presence penalty
- best of

To test the hypothesis that responses in https://www.kmeme.com/2020/10/gpt-3-bot-went-undetected-askreddit-for.html require carefully constructed presets.

Note that if you are running MacOS High Sierra, please add `export OBJC_DISABLE_INITIALIZE_FORK_SAFETY=YES` to your bash_profile.

Author: shreyashankar
Date: 13 October 2020
"""

CONFIG_VAR = "OPENAI_CONFIG"
KEY_NAME = "OPENAI_KEY"
POOL_SIZE = 10

# Housekeeping
env_vars = {}
with open(os.environ.get(CONFIG_VAR)) as f:
    for line in f:
        if line.startswith('#') or not line.strip():
            continue
        key, value = line.strip().split('=', 1)
        env_vars[key] = value.replace("'", "")

set_openai_key(env_vars[KEY_NAME])

# Perform grid search

param_grid = {
    'prompt': ["What story can you tell which won't let anyone sleep at night?"],
    'temperature': np.linspace(0.0, 1.0, 5),
    'frequency_penalty': np.linspace(0.0, 1.0, 5),
    'presence_penalty': np.linspace(0.0, 1.0, 5),
    'best_of': np.arange(1, 6)
}

grid = ParameterGrid(param_grid)
data = []
count = 0

def make_request(params):
    gpt = GPT(max_tokens=700, input_prefix="Q: ", output_prefix="A: ", temperature=params['temperature'].item())

    res = gpt.get_top_reply(params['prompt'], frequency_penalty=params['frequency_penalty'].item(), presence_penalty=params['presence_penalty'].item(), best_of=params['best_of'].item())

    # Add to responses
    params['result'] = res.replace("A: ", "")
    return params

params_list = [params for params in grid]
with Pool(POOL_SIZE) as p:
    data = p.map(make_request, params_list)

# Create df and dump to csv
df = pd.DataFrame(data)
df.to_csv('results.csv', index=False)
