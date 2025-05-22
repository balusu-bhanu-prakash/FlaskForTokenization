from nltk.tokenize import TreebankWordTokenizer

tokenizer = TreebankWordTokenizer()

def tokenize_text(text):
    if not text:
        return []
    return tokenizer.tokenize(text)
