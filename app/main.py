from dotenv import load_dotenv
import os

load_dotenv()

from fastapi import FastAPI
from app.models.request_models import TaskRequest
from app.services.workflow_manager import run_workflow

app = FastAPI()

@app.get("/")
def health():
    return {"status": "AI Multi-Agent Platform running"}

@app.post("/run-task")
def run_task(request: TaskRequest):

    result = run_workflow(request.data)

    return result