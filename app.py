from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()

class Question(BaseModel):
    question: str

# Hugging Face Inference API
HF_API_URL = "https://api-inference.huggingface.co/models/TinyLlama/TinyLlama-1.1B-Chat-v1.0"
HF_HEADERS = {"Authorization": "Bearer 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"}  # 👈 paste your HF token here

@app.get("/")
def home():
    return {"message": "ApsConnect AI Agent is live!"}

@app.post("/ask")
def ask(data: Question):
    q = data.question
    payload = {"inputs": q}

    # Send request to Hugging Face API
    response = requests.post(HF_API_URL, headers=HF_HEADERS, json=payload)

    if response.status_code == 200:
        try:
            output = response.json()[0]["generated_text"]
            return {"answer": output}
        except Exception:
            return {"answer": "Error: unexpected response format"}
    else:
        return {"answer": f"Error: {response.status_code}, {response.text}"}
