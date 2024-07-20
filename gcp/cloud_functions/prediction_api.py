from google.cloud import aiplatform
import numpy as np
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict_failure():
    data = request.get_json()
    input_data = np.array([[data['temperature'], data['vibration']]])
    model = aiplatform.Model('projects/your-project/models/predictive_model')
    prediction = model.predict(input_data)
    return jsonify(prediction.tolist())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
