from fastapi import FastAPI
from pydantic import BaseModel
import uuid
import requests
import os
from dotenv import load_dotenv
from pathlib import Path

# Load .env correctly
BASE_DIR = Path(__file__).resolve().parent
env_path = BASE_DIR / ".env"
load_dotenv(dotenv_path=env_path)

app = FastAPI()

N8N_WEBHOOK_URL = os.getenv("N8N_WEBHOOK_URL")

print("N8N_WEBHOOK_URL:", N8N_WEBHOOK_URL)


# Request model
class UserRequest(BaseModel):
    email: str
    text: str


@app.post("/process")
def process_text(data: UserRequest):

    if not N8N_WEBHOOK_URL:
        return {"error": "Webhook URL not found in .env"}

    session_id = str(uuid.uuid4())

    payload = {
        "email": data.email,
        "text": data.text,
        "session_id": session_id
    }

    try:
        response = requests.post(N8N_WEBHOOK_URL, json=payload)
        return {
            "message": "Workflow triggered successfully",
            "session_id": session_id,
            "n8n_response": response.text
        }

    except Exception as e:
        return {
            "error": str(e)
        }