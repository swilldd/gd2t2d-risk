from typing import Any, Dict
from fastapi import FastAPI
import uvicorn
from src.pipeline.predict import predict_single
from src.schemas.models import Patient, PredictResponse


app = FastAPI(title="GDM2T2DPredict")

@app.get("/")
def home():
    return {"message": "GD2T2D Risk Predicition Service"}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/predict", response_model=PredictResponse)
def predict(patient: Patient) -> PredictResponse:
    t2dm_prob = predict_single(patient.model_dump())
    return PredictResponse(
        t2dm_probability=t2dm_prob,
        t2dm_risk=bool(t2dm_prob >= 0.5)
    )
        

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9696)