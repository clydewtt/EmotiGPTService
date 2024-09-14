import os
import openai
from dotenv import load_dotenv
from emotionTypes import Emotions


def sentiment_analysis(user_input):
    load_dotenv()
    openai.api_key = os.getenv("OPENAI_API_KEY")
    messages = [
        {
            "role": "system",
            "content": f"You are a sentiment analysis tool, based on an emotion given in the user's user_input, you will return ONLY one of the following applicable emotions: {[emotion.value for emotion in Emotions]}",
        },
    ]
    if user_input:
        messages.append({"role": "user", "content": user_input})
        chat = openai.chat.completions.create(model="gpt-4o-mini", messages=messages)
        reply = chat.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
        return reply
    return "Please enter text for sentiment analysis"
