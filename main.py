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
from firebase.firebase import db
from firebase.collections import Collection

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

@app.put("/conversations/update/{conversation_id}")
def update_conversation(conversation_id: str):
    conversation_doc = db.collection(Collection.CONVERSATIONS).document(conversation_id).get()

    if not conversation_doc.exists:
        raise HTTPException(status_code=404, detail=f"Conversation {conversation_id} not found")
    
    current_messages = conversation_doc.to_dict().get("messages", [])

    current_messages.append({})


@app.get("/conversations/{user_id}")
def get_user_conversations(user_id: str):
    conversations = []
    conversations_ref = db.collection(Collection.CONVERSATIONS)
    user_doc = db.collection(Collection.USERS).document(user_id).get()

    if not user_doc.exists:
        raise HTTPException(status_code=404, detail=f"User {user_id} not found")
    
    conversation_ids = user_doc.to_dict().get("conversation_ids", [])

    for conversation_id in conversation_ids:
        conversation = conversations_ref.document(conversation_id).get()

        if conversation.exists:
            conversations.append(conversation)

    return {"user_id": user_id, "conversations": conversations}

conversation_history = []

@app.post("/chat")
def read_chat(request: EmotionRequest):
    global conversation_history
    user_request = request.user_input
    emotion_response = request.emotion_response
    
    if emotion_response not in Emotions.__members__.values():
        raise HTTPException(
            status_code=404, detail=f"{emotion_response} is not an applicable emotion."
        )
    
    sentiment_response = sentiment_analysis(user_request)
    
    reply, conversation_history = gpt_integration(
        user_request, emotion_response, sentiment_response, conversation_history
    )

    print(
        f"""User Request: {user_request},
        User's physical emotion: {emotion_response},
        Text sentiment analysis: {sentiment_response}"""
    )
    print(f"Assistant: {reply}")

    return {"message": reply}


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
    )
