from fastapi import FastAPI, Request
from pydantic import BaseModel
import requests

app = FastAPI()

class Question(BaseModel):
    question: str

@app.get("/")
def home():
    return {"message": "ApsConnect AI Agent is live!"}

@app.post("/ask")
def ask(data: Question):
    q = data.question
    # For now, just echo back
    answer = f"AI response for: {q}"
    return {"answer": answer}
