"""
Entry point for service
"""

import time
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
import uvicorn
from pydantic import BaseModel
from logger import logger
from emotion_types import Emotions
from sentiment_analysis import sentiment_analysis
from gptintegration import gpt_integration

app = FastAPI()


class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        start_time = time.time()
        response = await call_next(request)
        process_time = time.time() - start_time
        formatted_process_time = f"{process_time:.4f}"
        logger.info(
            "Request: %s %s completed in %ss",
            request.method,
            request.url.path,
            formatted_process_time,
        )
        return response


class EmotionRequest(BaseModel):
    user_input: str
    emotion_response: str


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


@app.post("/chat")
def read_chat(request: EmotionRequest):
    user_request = request.user_input
    emotion_response = request.emotion_response
    if emotion_response not in Emotions:
        raise HTTPException(
            status_code=404, detail=f"{emotion_response} is not an applicable emotion."
        )
    conversation_history = []
    sentiment_response = sentiment_analysis(user_request)

    reply, conversations = gpt_integration(
        user_request, emotion_response, sentiment_response, conversation_history
    )

    print(
        f"""User Request: {user_request},
        User's physical emotion: {emotion_response},
        Text sentiment analysis: {sentiment_response}"""
    )
    print(f"Assistant: {reply}")

    return {"message": reply}, conversations


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
    )
