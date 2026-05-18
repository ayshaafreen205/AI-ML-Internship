import streamlit as st
import joblib
import numpy as np
from sklearn.datasets import load_diabetes

model = joblib.load('model.pkl')
scaler = joblib.load('scaler.pkl')

diabetes = load_diabetes()

st.title("💉Diabetes Progession Prediction")
st.write("Enter the measurements below to predict Diabetes Progression.")


st.sidebar.header("📘 About the Project")
st.sidebar.info(
    "This app uses a Support Vector Machine (SVM) model trained on the Diabetes dataset. "
)
st.sidebar.write("🧋 Make your prediction below!")

age = st.number_input("Age", value=0.0)
sex = st.number_input("Sex", value=0.0)
bmi = st.number_input("BMI", value=0.0)
bp = st.number_input("Blood Pressure", value=0.0)

s1 = st.number_input("S1 (Total Serum Cholesterol)", value=0.0)
s2 = st.number_input("S2 (Low-Density Lipoproteins)", value=0.0)
s3 = st.number_input("S3 (High-Density Lipoproteins)", value=0.0)
s4 = st.number_input("S4 (Total Cholesterol / HDL)", value=0.0)
s5 = st.number_input("S5 (Log of Serum Triglycerides)", value=0.0)
s6 = st.number_input("S6 (Blood Sugar Level)", value=0.0)

if st.button("🔍 Predict"):
    input_data = np.array([[age, sex, bmi, bp,s1,s2,s3,s4,s5,s6]])
    scaled_input = scaler.transform(input_data)
    prediction = model.predict(scaled_input)[0]
    st.success(f"Predicted Diabetes : {prediction}")