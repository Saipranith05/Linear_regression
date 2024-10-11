import streamlit as st
import numpy as np
import joblib
model = joblib.load("tips.pkl")

st.title("App of Prediction")

total_bill = st.number_input("Please enter your total_bill", min_value =0.0, step = 0.1)
gender = st.selectbox("Sex",["Male","Female"])
smoker = st.selectbox("smoker", ["Yes", "No"])
day = st.selectbox("day", ["Thur", "Fri", "Sat", "Sun"])
time=st.selectbox("time",["Lunch","Dinner"])
size = st.number_input("Please enter your size", min_value=0, step=1)

gender_value = 0 if gender == "Male" else 1
smoker_value = 0 if smoker == "Yes" else 1
day_value = {"Thur":0, "Fri":1, "Sat":2, "Sun":3}[day]
time_value = 0 if time == "Lunch" else 1

if st.button("Predict"):
    result = model.predict([[total_bill,gender_value,smoker_value,day_value,time_value,size]])
    st.write(f"The predicted tip amount is ${result[0]:.2f}")   