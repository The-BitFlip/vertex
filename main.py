# app/main.py

from fastapi import FastAPI
from vertex.app.api.v1.endpoints import upload, sandbox
import os

app = FastAPI(
    title="Vertex Central Server",
    description="Your central server for file uploads and more.",
    version="1.0.0"
)

# Include the upload route under /api/v1
app.include_router(upload.router, prefix="/api/v1")
app.include_router(sandbox.router, prefix="/api/v1/sandbox")

# Ensure the upload directory exists
os.makedirs("uploads", exist_ok=True)

@app.get("/")
def read_root():
    return {"message": "Welcome to Vertex Central Server"}
