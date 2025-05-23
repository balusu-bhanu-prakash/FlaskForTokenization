# api/tokenize.py
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

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # default to 5000 if not set
    app.run(host='0.0.0.0', port=port)
