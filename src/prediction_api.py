from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open('src/model.pkl', 'rb'))
appliance_map = {'fan': 0, 'ac': 1, 'washing_machine': 2}

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    features = np.array([[data['vibration'], data['temperature'], data['current'], appliance_map[data['appliance']]]])
    prediction = model.predict(features)
    return jsonify({'needs_service': bool(prediction[0])})

if __name__ == '__main__':
    app.run(debug=True)
