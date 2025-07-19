from fastapi import FastAPI
from app.schema import DiabetesInput
from app.predict import make_prediction

app = FastAPI()

@app.post("/predict")
def predict_diabetes(data: DiabetesInput):
    result = make_prediction(data)
    return {"prediction": result}
