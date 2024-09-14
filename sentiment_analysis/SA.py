import openai
import os
from dotenv import load_dotenv
from emotionTypes import Emotions
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')


messages = [
    {"role": "system", "content": F"You are a sentiment analysis tool, based on an emotion given in the users input, you will return ONLY one of the following applicable emotions: {[emotion.value for emotion in Emotions]}"},
]

def chatbot(input):
    if input:
        messages.append({"role": "user", "content": input}) 
        chat = openai.chat.completions.create(
            model="gpt-4o-mini", messages=messages
        )
        reply = chat.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
        return reply

user_input = "Hello" #Example of passing string to function
print("AI:", chatbot(user_input))