## Setup
1. First, clone or fork this repository. Then to set up your virtual environment, do the following:

1. Create a virtual environment in the root directory: python -m venv \$ENV_NAME
1. Activate the virtual environment: source \$ENV_NAME/bin/activate (for MacOS, Unix, or Linux users) or .\\ENV_NAME\\Scripts\\activate (for Windows users)
1. Install requirements: pip install -r requirements.txt
1. To add your secret key: create a file anywhere on your computer called openai.cfg with the contents OPENAI_KEY=\$YOUR_SECRET_KEY, where \$YOUR_SECRET_KEY looks something like 'sk-somerandomcharacters' (including quotes). If you are unsure what your secret key is, navigate to the API docs and copy the token displayed next to the "secret" key type.
1. Set your environment variable to read the secret key: run export OPENAI_CONFIG=/path/to/config/openai.cfg (for MacOS, Unix, or Linux users)

Cloned from `https://github.com/shreyashankar/gpt3-sandbox`.