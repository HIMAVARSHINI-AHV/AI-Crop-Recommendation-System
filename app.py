import streamlit as st
import numpy as np
import joblib

model = joblib.load('rf_crop_model.pkl')
class_names = np.load('crop_classes.npy', allow_pickle=True) 

st.set_page_config(page_title="Crop Recommendation", layout="centered")
st.title("AI-Based Crop Recommendation System")
st.markdown("Enter soil and environmental values to get the best crop recommendation:")

N = st.slider('Nitrogen (N)', 0, 140, 50)
P = st.slider('Phosphorous (P)', 5, 145, 50)
K = st.slider('Potassium (K)', 5, 205, 50)
temperature = st.slider('Temperature (°C)', 10, 45, 25)
humidity = st.slider('Humidity (%)', 10, 100, 50)
ph = st.slider('Soil pH', 3, 10, 6)
rainfall = st.slider('Rainfall (mm)', 20, 300, 100)

if st.button("Recommend Crop"):
    input_data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
    prediction = model.predict(input_data)[0]
    recommended_crop = class_names[prediction]
    st.success(f"Recommended Crop: **{recommended_crop}**")
