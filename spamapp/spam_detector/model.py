import joblib
import numpy as np
import re

# Load the trained model and vectorizer from mlapp/models directory
model = joblib.load('E:\\spamapp\\mlapp\\models\\spam_model.pkl')  # Adjust this path accordingly
tfidf = joblib.load('E:\\spamapp\\mlapp\\models\\tfidf_vectorizer.pkl')  # Adjust this path accordingly

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    return text

def predict_message(message):
    processed_message = preprocess_text(message)
    
    # Transform the message using TfidfVectorizer
    message_tfidf = tfidf.transform([processed_message])  # This should already be in 2D format
    
    # Get predicted probability for the positive class (spam)
    prediction_proba = model.predict_proba(message_tfidf)[:, 1]
    threshold = 0.4
    prediction = (prediction_proba >= threshold).astype(int)

    return "Spam" if prediction[0] == 1 else "Not Spam", prediction_proba[0]