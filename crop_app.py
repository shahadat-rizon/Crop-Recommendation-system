import joblib
import pickle
import numpy as np
from flask import Flask, render_template, request, redirect
app = Flask(__name__)

crop_dict = {
    'rice': 1,
    'maize': 2,
    'chickpea': 3,
    'kidneybeans': 4,
    'pigeonpeas': 5,
    'mothbeans': 6,
    'mungbean': 7,
    'blackgram': 8,
    'lentil': 9,
    'pomegranate': 10,
    'banana': 11,
    'mango': 12,
    'grapes': 13,
    'watermelon': 14,
    'muskmelon': 15,
    'apple': 16,
    'orange': 17,
    'papaya': 18,
    'coconut': 19,
    'cotton': 20,
    'jute': 21,
    'coffee': 22
}

model_path = 'model.pkl'
loaded_model = joblib.load(model_path)

scaler_path = 'sd.pkl'
scaler = joblib.load(scaler_path)

@app.route('/')
def home():
    return render_template('Home_1.html')

@app.route('/Predict')
def prediction():
    return render_template('Index.html')

@app.route('/form', methods=["POST"])
def brain():
    Nitrogen=float(request.form['Nitrogen'])
    Phosphorus=float(request.form['Phosphorus'])
    Potassium=float(request.form['Potassium'])
    Temperature=float(request.form['Temperature'])
    Humidity=float(request.form['Humidity'])
    Ph=float(request.form['ph'])
    Rainfall=float(request.form['Rainfall'])
     
    values = np.array([[Nitrogen, Phosphorus, Potassium, Temperature, Humidity, Ph, Rainfall]])
    values_2d = scaler.transform(values).reshape(1, -1)

    if Ph>0 and Ph<=14 and Temperature<100 and Humidity>0: 
        arr = values_2d
        acc = loaded_model.predict(arr)
        print(acc)
        predicted_crop_code = acc[0]
        predicted_crop_name = [crop for crop, code in crop_dict.items() if code == predicted_crop_code][0]
        return render_template('prediction.html', prediction=predicted_crop_name)
    else:
        return "Sorry...  Error in entered values in the form Please check the values and fill it again"



if __name__ == '__main__':
    app.run(debug=True)















