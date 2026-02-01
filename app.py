import streamlit as st
import pickle
import numpy as np

st.title("Customer Churn Prediction")

# Load trained model
model = pickle.load(open("model.pkl", "rb"))

tenure = st.number_input("Tenure", 0, 72)
monthly_charges = st.number_input("Monthly Charges", 0.0, 200.0)
total_charges = st.number_input("Total Charges", 0.0, 10000.0)

if st.button("Predict"):
    data = np.array([[tenure, monthly_charges, total_charges]])
    prediction = model.predict(data)

    if prediction[0] == 1:
        st.error("Customer is likely to churn ❌")
    else:
        st.success("Customer will not churn ✅")
