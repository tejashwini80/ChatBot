import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import SVC
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from bot.preprocess import preprocess_text, load_intents

def train_model():
    intents = load_intents("bot/intents.json")
    labels, examples = [], []
    label_map = {}

    for idx, intent in enumerate(intents["intents"]):
        label_map[intent["tag"]] = idx
        for example in intent["examples"]:
            examples.append(preprocess_text(example))
            labels.append(idx)

    # Vectorize the text data
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(examples)
    y = labels

    # Train the model
    model = SVC(kernel='linear', probability=True)
    model.fit(X, y)

    # Save the model and vectorizer
    with open("bot/model.pkl", "wb") as model_file:
        pickle.dump(model, model_file)
    with open("bot/vectorizer.pkl", "wb") as vectorizer_file:
        pickle.dump(vectorizer, vectorizer_file)

    return model, vectorizer, label_map

if __name__ == "__main__":
    train_model()
