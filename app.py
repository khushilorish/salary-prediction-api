from fastapi import FastAPI
import pandas as pd
import joblib
import os
from feature_engineering import FeatureEngineering
from pydantic import BaseModel

# print("Current Folder:", os.getcwd())
# print("Files:", os.listdir())

app = FastAPI()

model = joblib.load("salary_prediction_pipeline.pkl")

class SalaryInput(BaseModel):
    job_title: str
    industry:str
    location: str
    remote_work: str
    education_level: str
    company_size: str
    experience_years: int
    skills_count: int
    certifications: int

@app.get("/")
def home():
    return {"message": "Salary Prediction API is running"}

@app.post("/predict")
def predict(data: SalaryInput):
    input_df = pd.DataFrame([data.model_dump()])

    prediction = model.predict(input_df)

    return {"predicted_salary": float(prediction[0])}