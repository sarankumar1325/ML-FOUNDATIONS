from flask import Flask, request, jsonify
import numpy as np
import pickle
import os

app = Flask(__name__)

# Load the model and scaler
with open('iris_model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get features from JSON request
        data = request.get_json()
        features = np.array([
            data['sepal_length'],
            data['sepal_width'],
            data['petal_length'],
            data['petal_width']
        ]).reshape(1, -1)

        # Scale features
        features_scaled = scaler.transform(features)

        # Make prediction
        prediction = model.predict(features_scaled)
        probability = model.predict_proba(features_scaled)

        # Get class name
        class_names = ['setosa', 'versicolor', 'virginica']
        predicted_class = class_names[prediction[0]]

        return jsonify({
            'prediction': predicted_class,
            'probability': probability[0].tolist(),
            'status': 'success'
        })

    except Exception as e:
        return jsonify({
            'error': str(e),
            'status': 'error'
        })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
