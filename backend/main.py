from fastapi import FastAPI
from pydantic import BaseModel
import uuid
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

N8N_WEBHOOK_URL = os.getenv("N8N_WEBHOOK_URL")

class UserRequest(BaseModel):
    email: str
    text: str

@app.post("/process")
def process_text(data:UserRequest):
    session_id = str(uuid.uuid4())

    paylod = {
        'email': data.email,
        'text' : data.text,
        'session_id' : session_id
    }

    response = requests.post(N8N_WEBHOOK_URL, json=paylod)

    return {
        'message': 'Workflow triggered',
        'session_id': session_id,
        'n8n_response': response.text
    }