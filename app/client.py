from flask import Flask, jsonify
import requests
import pandas as pd
import numpy as np


X = pd.read_csv('app/data/x_eval.csv')

n = np.random.randint(0, X.shape[0])
feature = list(X.loc[n].values)


if __name__ == '__main__':
    r = requests.post('http://localhost/predict', json=feature)
    print(f'Status: {r.status_code}')

    if r.status_code == 200:
        print(f"Prediction: {r.json()}")   
    else:
        print(r.text) 
