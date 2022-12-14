# -*- coding: utf-8 -*-
"""app.py.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1B4boReWJBztpsOg-B1wyirZ0ai2kAXQE
"""

import pickle
import joblib
import random

import numpy as np
from flask import Flask, jsonify, render_template, request
from pathlib import Path

app = Flask(__name__)
model=joblib.load(open("engine_model.pkl","rb"))

@app.route('/')
def predict():
    return render_template('/content/Maunal predict.html')
@app.route('/y_predict',methods=['POST','GET'])
def y_predict():
    x_test = [[int (x) for x in request.form.values()]]
    print(x_test)
    a=model.predict(x_test)
    pred = a[0]
    if(pred == 0):
        pred ="No failure expected within 30 days. "
    else:
        pred = "Maintenance Required!! Expected a failure within 30 days. "
    return render_template('Manual_predict.html', prediction_text=pred)

if (__name__=='__main__'):
    app.run(debug=True)