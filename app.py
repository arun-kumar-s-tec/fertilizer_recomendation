import streamlit as st
import pandas as pd
import joblib

# Load models
model = joblib.load('decision_tree_model.pkl')
crop_encoder = joblib.load('crop_encoder.pkl')
fertilizer_encoder = joblib.load('fertilizer_encoder.pkl')

# Page configuration
st.set_page_config(
    page_title="Fertilizer Recommendation System",
    page_icon="🌱",
    layout="centered"
)

# Title
st.title("🌱 Fertilizer Recommendation System")
st.write(
    "Predict the best fertilizer based on soil nutrients, "
    "climate conditions and crop type."
)

# Crop list
crop_options = list(crop_encoder.classes_)

# Inputs
st.header("Enter Soil and Crop Information")

crop = st.selectbox(
    "Select Crop",
    crop_options
)

N = st.number_input(
    "Nitrogen (N)",
    min_value=0,
    max_value=200,
    value=50
)

P = st.number_input(
    "Phosphorus (P)",
    min_value=0,
    max_value=200,
    value=50
)

K = st.number_input(
    "Potassium (K)",
    min_value=0,
    max_value=300,
    value=50
)

temperature = st.number_input(
    "Temperature (°C)",
    value=25.0
)

humidity = st.number_input(
    "Humidity (%)",
    value=70.0
)

ph = st.number_input(
    "Soil pH",
    value=6.5
)

rainfall = st.number_input(
    "Rainfall (mm)",
    value=100.0
)

# Prediction
if st.button("Recommend Fertilizer"):

    crop_encoded = crop_encoder.transform([crop])[0]

    data = pd.DataFrame({
        'N':[N],
        'P':[P],
        'K':[K],
        'temperature':[temperature],
        'humidity':[humidity],
        'ph':[ph],
        'rainfall':[rainfall],
        'label':[crop_encoded]
    })

    prediction = model.predict(data)

    fertilizer = fertilizer_encoder.inverse_transform(
        prediction
    )[0]

    st.success(
        f"Recommended Fertilizer: {fertilizer}"
    )