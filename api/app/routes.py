from flask import request, jsonify
from flask_cors import CORS
import openai

from app import app
CORS(app)

@app.route("/translate", methods=['GET', 'POST'])
def translate():
    prompt = request.json['prompt']
    # TODO:// configure openai request
    return {'text':prompt} 
