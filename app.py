import streamlit as st
import numpy as np
import tensorflow as tf
import pandas as pd 
import joblib
from sklearn.preprocessing import StandardScaler

# load the trained model
@st.cache_resource
def load_model():
    return tf.keras.models.load_model("Trained Model/churn_prediction_model.keras")
model = load_model()

# load the saved scaler 
scaler = joblib.load("Scaler/scaler.pkl")
st.title("Customer Churn Prediciton")
st.markdown("<h6 style='text-align: right; color: gray;'>Developed by Abhishek</h6>", unsafe_allow_html=True)

st.write("Enter customer details to predict churn")

# creating input fields
input = []
dataset = pd.read_csv("Dataset/Churn_Modelling.csv")
dataset.drop(["RowNumber","Empty","CustomerId","Geography","Gender"], axis = 1, inplace = True)
columns = [
    ("Credit Score", "CreditScore", 650),
    ("Age", "Age", 30),
    ("Tenure (Years)", "Tenure", 5),
    ("Account Balance", "Balance", 100000),
    ("Number of Products", "NumOfProducts", 1),
    ("Has Credit Card (1=Yes, 0=No)", "HasCrCard", 1),
    ("Is Active Member (1=Yes, 0=No)", "IsActiveMember", 1),
    ("Estimated Salary", "EstimatedSalary", 50000)
]
for label, col, default in columns:
    value = st.number_input(label, value=float(default), format="%.2f")
    input.append(value)

if st.button("Predict Churn"):
    input_array = np.array([input])
    input_scaled = scaler.transform(input_array)
    prediction = model.predict(input_scaled)
    result = "Churn" if prediction[0][0]>0.5 else "No Churn"
    st.write(f"### Prediction: {result}")

