from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Question(BaseModel):
    question: str

# Simple FAQ knowledge base
FAQ = {
    "exam date": "The internal exams are scheduled from 15th to 20th September.",
    "attendance rule": "Students must maintain 75% attendance to be eligible for exams.",
    "fees last date": "The last date to pay fees is 5th October.",
    "library timing": "The library is open from 9 AM to 6 PM on weekdays.",
    "holiday list": "The holiday list is available on the college notice board and app.",
    "event calendar": "College cultural fest is scheduled in December."
}

@app.get("/")
def home():
    return {"message": "ApsConnect AI Agent is live!"}

@app.post("/ask")
def ask(data: Question):
    q = data.question.lower()
    for key, answer in FAQ.items():
        if key in q:
            return {"answer": answer}
    return {"answer": "Sorry, I don’t know that yet. Please check with the college office."}
