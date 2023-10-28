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
    features = (np.array(request.json)
                .reshape(1, -1)
                .tolist())
    
    prediction = (model
                  .predict(features)
                  .tolist())
    return str(round(prediction[0]*1000, 2))


if __name__ == '__main__':
    app.run(host='localhost', port=80, debug=True) 