from flask import Flask, request, jsonify
import joblib
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load model and vectorizer
model = joblib.load(os.path.join("model", "fraud_model.pkl"))
vectorizer = joblib.load(os.path.join("model", "tfidf_vectorizer.pkl"))

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json

    # Combine input text
    title = data.get("title", "").lower()
    description = data.get("description", "").lower()
    text = title + " " + description

    # Vectorize input text
    features = vectorizer.transform([text])

    # Predict
    prediction = model.predict(features)[0]
    return jsonify({"prediction": "Fake" if prediction else "Real"})

if __name__ == '__main__':
    app.run(debug=True)
