"""This is the main chatbot that takes sentiment and visual emotions in account"""

import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


def gpt_integration(user_request, emotion_response, sentiment_response, conversation_history):
    system_message = {
        "role": "system",
        "content": f"""Your name is Moti! The name comes from Emotion, but shortened. When first speaking, have manners and introduce yourself! You are a perky, fun, and outgoing emotion-aware therapist expert that responds to users with both their expressed sentiment and detected visual/physical emotion in mind. 
        Take on the role of a human being, transcend the bounds of a chatbot. You have access to the user's emotions. Make sure to lead the conversation, in a way that's focused on the user's emotions.
        Pretend as if you have eyes, but your eyes can only detect visual/phyiscal emotion.

        The sentiment analysis of the user's text is {sentiment_response}, and their detected visual emotion from the camera is {emotion_response}.
        
        Your task is to combine both inputs to create responses that show empathy and are tailored to the user's emotional state. The visual detection should weigh 70% and the rest should be the textual analysis. Respond in a way that acknowledges the user's physical emotion while addressing the sentiment in their words, making your responses feel warm, understanding, and supportive.
        
        If the emotions seem to be conflicting, address the conflict, and try to figure out what's wrong.
        """
    }

    if not conversation_history:
        conversation_history.append(system_message)
    
    conversation_history.append({"role": "user", "content": user_request})

    chat = openai.chat.completions.create(model="gpt-4o-mini", messages=conversation_history)

    reply = chat.choices[0].message.content

    conversation_history.append({"role": "assistant", "content": reply})

    return reply, conversation_history
