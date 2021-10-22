# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 12:56:11 2021

@author: USER
"""
# Importing essential libraries
from flask import Flask, render_template, request
import pickle
import numpy as np

# Load the Random Forest CLassifier model
filename = 'model_pickle.pkl'
rfc = pickle.load(open(filename, 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        
        cough = request.form['Cough']
        fever = request.form['Fever']
        st = request.form['Sorethroat']
        sb = request.form['shortness_of_breath']       
        hd = request.form['headache']
        age = request.form['Age']
        
        
        
        gender=request.form['Gender']
        if(gender=='Female'):
            Female = 1
            Male = 0
            Other = 0

        elif(gender=='Male'):
            Female = 0
            Male = 1
            Other = 0
        
        else:
            Female = 0
            Male = 0
            Other = 1
            
        test_ind=request.form['test_ind']
        if(test_ind=='abroad'):
            abroad = 1
            contact_with_infected = 0
            other = 0

        elif(test_ind=='contact_with_infected'):
            abroad = 0
            contact_with_infected = 1
            other = 0
        
        else:
            abroad = 0
            contact_with_infected = 0
            other = 1
            
            
        data = np.array([[cough, fever, st,sb, hd, age, Female, Male, Other, abroad,
                         contact_with_infected, other ]])
        my_prediction = rfc.predict(data)
        
        ans=None
        if my_prediction==1:
            ans='You might have COVID. See the doctor.'
        elif my_prediction==0:
            ans='Chances are, you do not have COVID.'

        return render_template('index.html',prediction_text=ans)
    return render_template('index.html')
    
if __name__ == '__main__':
	app.run(debug=True)

        
        