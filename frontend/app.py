import streamlit as st
import requests


st.set_page_config(page_title="Diabetes Prediction", page_icon="🏥")

st.title("🏥 Diabetes Prediction System")
st.markdown("Enter the patient's clinical data below to get a prediction.")

col1, col2 = st.columns(2)

with col1:
    pregnancies = st.number_input("Pregnancies", min_value=0, step=1, value=1)
    glucose = st.number_input("Glucose", min_value=0.0, value=120.0)
    blood_pressure = st.number_input("Blood Pressure", min_value=0.0, value=70.0)
    skin_thickness = st.number_input("Skin Thickness", min_value=0.0, value=20.0)

with col2:
    insulin = st.number_input("Insulin", min_value=0.0, value=80.0)
    bmi = st.number_input("BMI", min_value=0.0, value=25.0)
    dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0, format="%.3f", value=0.5)
    age = st.number_input("Age", min_value=1, step=1, value=30)


if st.button("Predict Outcome"):
 
    API_URL = "http://localhost:8000/predict"
    
    payload = {
        "Pregnancies": pregnancies,
        "Glucose": glucose,
        "BloodPressure": blood_pressure,
        "SkinThickness": skin_thickness,
        "Insulin": insulin,
        "BMI": bmi,
        "DiabetesPedigreeFunction": dpf,
        "Age": age
    }

    try:
        response = requests.post(API_URL, json=payload)
        if response.status_code == 200:
            result = response.json()
            
            st.divider()
            if result["prediction"] == 1:
                st.error(f"Prediction: **{result['outcome']}**")
            else:
                st.success(f"Prediction: **{result['outcome']}**")
                
            st.info(f"Confidence Level: **{result['confidence'] * 100:.2f}%**")
        else:
            st.error("Error: Could not connect to the Prediction API.")
    except Exception as e:
        st.error(f"Connection Failed: {e}")

