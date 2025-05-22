# api/tokenize.py
from flask import Flask, request, jsonify
from nltk.tokenize import TreebankWordTokenizer

app = Flask(__name__)
tokenizer = TreebankWordTokenizer()


@app.route("/tokenize", methods=["POST"])
def tokenize_text():
    data = request.get_json()
    text = data.get("text", "")
    tokens = tokenizer.tokenize(text)
    return jsonify({"tokens": tokens})
