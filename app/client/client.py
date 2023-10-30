import requests
import pandas as pd
import numpy as np
from time import sleep

sleep(5)

# клиентское приложение использует заранее подготовленные данные
# выбирает из таблицы случайный объект и передает его нв сервер
X = pd.read_csv('data/x_eval.csv')

n = np.random.randint(0, X.shape[0]-1)
feature = list(X.loc[n].values)

# если между приложениями установлена связь, предсказание будет выведена на экран
if __name__ == '__main__':
    r = requests.post('http://localhost/predict', json=feature)
    print(f'Status: {r.status_code}')

    if r.status_code == 200:
        print(f"Prediction: {r.json()}")   
    else:
        print(r.text) 
