from flask import Flask

app = Flask(__name__)
app.config.from_envvar('LATEX_TRANSLATOR_CONFIG')

from app import routes
