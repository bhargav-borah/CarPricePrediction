import streamlit as st
import pickle
import pandas as pd

# Load the model
with open('LinearRegressionModel.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

st.title('Car Price Prediction')

# Input form
name = st.text_input('Car Name')
company = st.text_input('Company')
year = st.number_input('Year', min_value=1950, max_value=2023)
kms_driven = st.number_input('Kilometers Driven')
fuel_type = st.selectbox('Fuel Type', ['Petrol', 'Diesel', 'LPG'])


# Prepare input data
input_data = pd.DataFrame({
    'name': [name],
    'company': [company],
    'year': [year],
    'kms_driven': [kms_driven],
    'fuel_type': [fuel_type]
})

# Predict price
prediction = model.predict(input_data)[0]

# Display prediction
st.subheader('Predicted Price')
st.write(f'${prediction:.2f}')
