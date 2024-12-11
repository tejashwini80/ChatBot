import nltk
from nltk.tokenize import word_tokenize
import json

nltk.download('punkt')
nltk.download('punkt_tab')

def preprocess_text(text):
    return ' '.join(word_tokenize(text.lower()))

def load_intents(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)
