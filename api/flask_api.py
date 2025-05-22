# flask_api.py
from flask import Flask, request, jsonify
from tokenizer import tokenize_text  # your custom tokenizer function

app = Flask(__name__)

@app.route("/tokenize", methods=["POST"])
def tokenize():
    data = request.get_json()
    text = data.get("text", "")
    tokens = tokenize_text(text)
    return jsonify({"tokens": tokens})
