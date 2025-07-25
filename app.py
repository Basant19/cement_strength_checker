

from flask import Flask, render_template, request, jsonify
import numpy as np
import joblib
import os
from src.logger import logging

app = Flask(__name__)

# Load model and preprocessor
MODEL_PATH = os.path.join("artifacts", "model.pkl")
PREPROCESSOR_PATH = os.path.join("artifacts", "preprocessor.pkl")

try:
    model = joblib.load(MODEL_PATH)
    preprocessor = joblib.load(PREPROCESSOR_PATH)
    logging.info("Model and Preprocessor loaded successfully.")
except Exception as e:
    logging.error(f"Failed to load model or preprocessor: {e}")
    model = None
    preprocessor = None

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        # Extract features
        features = [
            data["cement"],
            data["blast_furnace_slag"],
            data["fly_ash"],
            data["water"],
            data["superplasticizer"],
            data["coarse_aggregate"],
            data["fine_aggregate"],
            data["age"]
        ]

        # Reshape and transform
        input_array = np.array(features).reshape(1, -1)
        transformed_input = preprocessor.transform(input_array)

        # Make prediction
        prediction = model.predict(transformed_input)[0]

        return jsonify({"prediction": round(prediction, 2)})

    except Exception as e:
        logging.error(f"Prediction failed: {e}")
        return jsonify({"error": str(e)}), 500
    


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
