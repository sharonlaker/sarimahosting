# -*- coding: utf-8 -*-


import numpy as np
import pickle
import pandas as pd
import streamlit as st 

from PIL import Image



file = open("sarima.pkl", 'rb')
res = pickle.load(file)



def welcome():
    return "Welcome All"

def predict_water_demand(duration):
    
    """Let's Authenticate the Banks Note 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: variance
        in: query
        type: number
        required: true
      - name: skewness
        in: query
        type: number
        required: true
      - name: curtosis
        in: query
        type: number
        required: true
      - name: entropy
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
        
    """
   

    prediction = res.forecast(n_period=())
    print(prediction)
    return(prediction)
   




def main():
    st.title("water demand")

    duration = st.text_input("duration","Type Here")
   
    result=""
    if st.button("Predict"):
        result=predict_water_demand(duration)
    st.success('{}'.format(result))
   

if __name__=='__main__':
    main()
    
    