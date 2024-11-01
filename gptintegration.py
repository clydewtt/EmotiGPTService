"""This is the main chatbot that takes sentiment and visual emotions in account"""

import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


def gpt_integration(user_request, emotion_response, sentiment_response, conversation_history):
    conversation_history.append({"role": "user", "content": user_request})

    system_message = {
        "role": "system",
        "content": f"""You are a normal chatbot that takes 
        sentiment analysis as input which is {sentiment_response}.
        You will also respond with the user's actual 
        physical emotion in mind, which is {emotion_response}.""",
    }

    if not any(msg["role"] == "system" for msg in conversation_history):
        conversation_history.insert(0, system_message)

    chat = openai.chat.completions.create(model="gpt-4o-mini", messages=conversation_history)

    reply = chat.choices[0].message.content

    conversation_history.append({"role": "assistant", "content": reply})

    return reply, conversation_history
