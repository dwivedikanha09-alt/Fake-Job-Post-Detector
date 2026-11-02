from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI()
model = joblib.load("model.pkl")


class Job(BaseModel):
    title: str = ""
    company_profile: str = ""
    description: str = ""
    requirements: str = ""
    employment_type: str = "Unknown"
    required_experience: str = "Unknown"
    required_education: str = "Unknown"
    telecommuting: int = 0
    has_company_logo: int = 0
    has_questions: int = 0


@app.get("/")
def home():
    return FileResponse("index.html")   # index.html, app.py ke same folder me


@app.post("/predict")
def predict(job: Job):
    text = " ".join([job.title, job.company_profile,
                     job.description, job.requirements])

    row = pd.DataFrame([{
        "text": text,
        "employment_type": job.employment_type,
        "required_experience": job.required_experience,
        "required_education": job.required_education,
        "telecommuting": job.telecommuting,
        "has_company_logo": job.has_company_logo,
        "has_questions": job.has_questions,
    }])

    prob = float(model.predict_proba(row)[0][1])
    return {"prediction": int(prob >= 0.5), "probability": prob}