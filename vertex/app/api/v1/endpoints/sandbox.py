# app/api/v1/endpoints/sandbox.py

from fastapi import APIRouter
from datetime import datetime

router = APIRouter()

@router.get("/ping")
def ping():
    return {"message": "pong", "timestamp": datetime.now().isoformat()}

@router.get("/dummy-data")
def dummy_data():
    return {
        "user": {
            "id": 123,
            "name": "Test User",
            "email": "test@example.com"
        },
        "status": "active",
        "features": ["upload", "logging", "api"]
    }
