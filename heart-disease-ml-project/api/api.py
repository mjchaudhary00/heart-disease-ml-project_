from fastapi import FastAPI
import joblib
import numpy as np

app = FastAPI()
model = joblib.load("models/best_model_xgboost.pkl")

@app.post("/predict")
def predict(data: dict):
    arr = np.array([[data[k] for k in data]])
    score = model.predict_proba(arr)[0][1]
    return {"risk_score": float(score)}
