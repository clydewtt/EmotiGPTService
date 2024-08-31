from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
import uvicorn
import time


app = FastAPI()

class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        start_time = time.time()
        response = await call_next(request)
        process_time = time.time() - start_time
        formatted_process_time = f'{process_time:.4f}'
        print(f"Request: {request.method} {request.url.path} completed in {formatted_process_time}s")
        return response

app.add_middleware(LoggingMiddleware)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Tentative
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],  # Tentative
)

@app.get("/")
def read_root():
    return {"message": "Connected to EmotiGPT-Service"}


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
    )