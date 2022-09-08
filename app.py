# -*- coding: utf-8 -*-


from flask import Flask,request
from flask_restful import Resource, Api
import pickle
#import json
#import csv
#from sklearn.tree import DecisionTreeRegressor
import pandas as pd
from flask_cors import CORS
#import warnings



app = Flask(__name__)
#
file = open("sarima.pkl", 'rb')
res = pickle.load(file)

CORS(app)
# creating an API object
@app.route('/')
def home():
    return 'welcome to the SWAP system prediction models'

@app.route("/predict", methods = ["GET"])
def predict():
    duration = request.args.get('duration')
    
    df = int(duration)
    prediction = res.forecast(df)
        #prediction = int(prediction[0])
    return str(prediction)

if __name__ == '__main__':
     app.run(port=8080)