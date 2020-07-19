from flask import request, jsonify
import openai

from app import app

@app.route("/translate", methods=['GET', 'POST'])
def translate_to_latex():
    text = request.form['prompt']
    # TODO:// configure openai request
    response = jsonify({'text': text}) 
    return response
