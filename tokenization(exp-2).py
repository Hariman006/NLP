import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt')
def tokenize_text(text):
    tokens = word_tokenize(text)
    return tokens
sample_inputs = [
    "Hi I am Hari.",
    "And I love to play games,",
    "Also I always listern to Songs."
]
for text in sample_inputs:
    print("Input Text:", text)
    tokens = tokenize_text(text)
    print("Tokens:", tokens)
    print("----------------------------")