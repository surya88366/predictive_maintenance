import streamlit as st
import requests

st.title("Appliance Health Monitor")

appliance = st.selectbox("Select Appliance", ["fan", "ac", "washing_machine"])
vibration = st.slider("Vibration", 0, 100, 50)
temperature = st.slider("Temperature", 10, 80, 40)
current = st.slider("Current", 0.0, 6.0, 2.5)

if st.button("Predict"):
    payload = {
        "appliance": appliance,
        "vibration": vibration,
        "temperature": temperature,
        "current": current
    }
    response = requests.post("https://your-api-url.onrender.com/predict", json=payload)
    result = response.json()
    st.success(f"Needs Service: {result['needs_service']}")
