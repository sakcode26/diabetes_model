# app/predict.py
import pickle
import numpy as np

# Load the model once
model = pickle.load(open("app/diabetes_model.pkl", "rb"))

def make_prediction(data):
    input_data = np.array([[data.pregnancies, data.glucose, data.bloodpressure,
                            data.skinthickness, data.insulin, data.bmi, data.dpf, data.age]])
    prediction = model.predict(input_data)[0]
    return "Diabetic" if prediction == 1 else "Not Diabetic"
