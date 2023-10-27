from flask import Flask
import requests
import pandas as pd

X = pd.read_pickle('app/data/x_eval.pkl')
y = pd.read_pickle('app/data/y_eval.pkl')


if __name__ == '__main__':
    r = requests.post('http://localhost/predict', json=X)
    print(f'Status: {r.status_code}')

    if r.status_code == 200:
        print(f"Prediction: {r.json()}")
        
        if r.json() == y.to_json():
            print('It works!')
        else:
            print(f'Errors in {set(r.json() & set(y.to_json()))}')
            
    else:
        print(r.text) 

