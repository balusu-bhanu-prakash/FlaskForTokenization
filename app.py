from flask import Flask, request, jsonify
from nltk.tokenize import TreebankWordTokenizer
import os

app = Flask(__name__)
tokenizer = TreebankWordTokenizer()


@app.route("/tokenize", methods=["POST"])
def tokenize_text():
    data = request.get_json()
    text = data.get("text", "")
    tokens = tokenizer.tokenize(text)
    return jsonify({"tokens": tokens})


@app.route("/", methods=["GET"])
def index():
    return jsonify({"message": "Flask tokenization API is up and running!"})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # default to 5000 for local
    app.run(host="0.0.0.0", port=port)
