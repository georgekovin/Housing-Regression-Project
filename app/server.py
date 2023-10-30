from flask import Flask, request
import pickle
import numpy as np

# инициализация приложения
app = Flask(__name__)


# расконсервация модели из pickle
with open('app/models/model.pkl', 'rb') as f:
    model = pickle.load(f)


# домашняя страница с сообщением о том, что сервер работает
@app.route('/')
def index():
    return "Test message. The server is running."


# страница с моделью, которая принимает данные и выдает
@app.route('/predict', methods=['POST'])
def predfunc():
    features = (np.array(request.json)
                .reshape(1, -1)
                .tolist())
    
    prediction = (model
                  .predict(features)
                  .tolist())
    
    # переводим цену из тысяч долларов в просто доллары и центы
    return str(round(prediction[0]*1000, 2))


# приложение запущено на localhost
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True) 