# Importing essential libraries
from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd

# Load the Random Forest CLassifier model
filename = 'diabetes-prediction-rfc-model.pkl'
classifier = pickle.load(open(filename, 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        age = int(request.form['Age'])
        gender = str(request.form['Gender'])
        polyu = str(request.form['Polyuria'])
        polyd = str(request.form['Polydipsia'])
        Suwl = int(request.form['Sudden_weight_loss'])
        waek = int(request.form['Weakness'])
        polyp = int(request.form['Polyphagia'])
        genth = int(request.form['Genital_thrush'])
        viblu = int(request.form['Visual_blurring'])
        itching = int(request.form['Itching'])
        irriti = int(request.form['Irritability'])
        dehea = int(request.form['Delayed_healing'])
        parpa = int(request.form['Partial_paresis'])
        musstiff = int(request.form['Muscle_stiffness'])
        alopecia = int(request.form['Alopecia'])
        obesity = int(request.form['Obesity'])
        
        data = pd.DataFrame([[age, gender, polyu, polyd, Suwl, waek, polyp, genth, viblu,
                          itching, irriti, dehea, parpa, musstiff, alopecia, obesity]])
        my_prediction = classifier.predict(data)
        
        return render_template('result.html', prediction=my_prediction)

if __name__ == '__main__':
	app.run(debug=True)
