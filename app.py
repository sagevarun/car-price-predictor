import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load the trained model
model = pickle.load(open('LinearRegressionModel.pkl', 'rb'))

# Title and Description
st.title("Car Price Prediction App")
st.markdown("This app predicts the price of a car based on its features!")

# User inputs
name = st.text_input("Car Name", "e.g., Maruti Swift")
company = st.selectbox("Car Company", ["Maruti", "Hyundai", "Honda", "Toyota", "Ford", "BMW", "Audi"])
year = st.number_input("Year of Manufacture", min_value=1980, max_value=2023, step=1)
kms_driven = st.number_input("Kms Driven", min_value=0, max_value=1000000, step=1000)
fuel_type = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG", "LPG", "Electric"])

# Create a DataFrame for the input
input_data = pd.DataFrame({
    'name': [name],
    'company': [company],
    'year': [year],
    'kms_driven': [kms_driven],
    'fuel_type': [fuel_type]
})

# Show the input data
st.write("Input data:")
st.write(input_data)

# Predict the price
if st.button("Predict Price"):
    try:
        prediction = model.predict(input_data)[0]
        st.success(f"The predicted price of the car is ₹{prediction:,.2f}")
    except Exception as e:
        st.error(f"Error: {e}")

