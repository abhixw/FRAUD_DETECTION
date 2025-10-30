import streamlit as st
import numpy as np
import pandas as pd
import joblib

# Load model and scaler
model = joblib.load("model/fraud_model.pkl")
scaler = joblib.load("model/scaler.pkl")

st.set_page_config(page_title="Fraud Detection App", layout="wide")
st.title("💳 Fraud Detection System")
st.write("Enter the transaction details below to check if it might be fraudulent.")

# Define all required columns as per your dataset
columns = [
    'Time', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'V10',
    'V11', 'V12', 'V13', 'V14', 'V15', 'V16', 'V17', 'V18', 'V19', 'V20',
    'V21', 'V22', 'V23', 'V24', 'V25', 'V26', 'V27', 'V28', 'Amount'
]

# Sidebar input fields
st.sidebar.header("🧮 Input Features")
user_inputs = []

for col in columns:
    val = st.sidebar.number_input(f"{col}", value=0.0)
    user_inputs.append(val)

# Convert user inputs to a DataFrame
input_data = pd.DataFrame([user_inputs], columns=columns)

# Predict button
if st.sidebar.button("🔍 Predict"):
    # Scale the input
    scaled_input = scaler.transform(input_data)
    prediction = model.predict(scaled_input)[0]
    
    # Display result
    st.subheader("Prediction Result:")
    if prediction == 1:
        st.error("🚨 Fraud Detected! This transaction seems suspicious.")
    else:
        st.success("✅ Transaction appears safe.")
else:
    st.info("👈 Enter details in the sidebar and click **Predict** to see results.")
