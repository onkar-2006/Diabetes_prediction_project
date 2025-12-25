from fastapi import FastAPI, HTTPException
from model import PatientData
import joblib
import numpy as np
from pathlib import Path
from fastapi import FastAPI


BASE_DIR = Path(__file__).resolve().parent 

MODEL_DIR = BASE_DIR.parent / "model"

MODEL_PATH = MODEL_DIR / "gradient_boosting_model.pkl" 
SCALER_PATH = MODEL_DIR / "scaler.pkl"

try:
    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)
except Exception as e:
    print(f"❌ Error loading files: {e}")


app = FastAPI(title="Diabetes Prediction API")

@app.get("/")
def home():
    return {"message": "Diabetes Prediction API is running!"}

@app.post("/predict")
def predict_diabetes(data: PatientData):
    try:
        input_data = [
            data.Pregnancies, data.Glucose, data.BloodPressure, 
            data.SkinThickness, data.Insulin, data.BMI, 
            data.DiabetesPedigreeFunction, data.Age
        ]
        
        input_array = np.array(input_data).reshape(1, -1)

        scaled_input = scaler.transform(input_array)
        
        prediction = model.predict(scaled_input)
        probability = model.predict_proba(scaled_input)
        
        return {
            "prediction": int(prediction[0]),
            "outcome": "Positive" if prediction[0] == 1 else "Negative",
            "confidence": round(float(np.max(probability)), 4)
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# To run: uvicorn main:app --reload