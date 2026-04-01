from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()

# Load model & scaler
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")

# Input schema
class InputData(BaseModel):
    age: int
    gender: str
    tenure: int
    monthly_charges: float

@app.post("/predict")
def predict(data: InputData):
    try:
        # Convert gender to numeric
        gender_val = 1 if data.gender.lower() == "female" else 0

        # Prepare input
        X = np.array([[data.age, gender_val, data.tenure, data.monthly_charges]])
        X_scaled = scaler.transform(X)

        # Prediction
        pred = model.predict(X_scaled)[0]

        # Confidence score
        proba = model.predict_proba(X_scaled)[0][1]

        return {
            "prediction": int(pred),
            "label": "Churn" if pred == 1 else "Not Churn",
            "confidence": round(proba, 2)
        }

    except Exception:
        raise HTTPException(status_code=500, detail="Model error")