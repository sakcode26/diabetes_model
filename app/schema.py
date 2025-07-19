# app/schema.py
from pydantic import BaseModel

class DiabetesInput(BaseModel):
    pregnancies: int
    glucose: int
    bloodpressure: int
    skinthickness: int
    insulin: int
    bmi: float
    dpf: float
    age: int
