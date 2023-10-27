from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)


with open('app/models/model.pkl', 'rb') as f:
    model = pickle.load(f)


@app.route('/')
def index():
    return "Test message. The server is running."


@app.route('/predict', methods=['POST'])
def predfunc():
    features = np.array(request.json)
    pred = model.predict(features)
    
    return jsonify({"prediction": pred})


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True) 