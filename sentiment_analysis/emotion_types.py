"""This class contains all the emotions specified from FaceAPI"""
from enum import Enum

class Emotions(Enum):
    NEUTRAL = "Neutral"
    HAPPY = "Happy"
    SAD = "Sad"
    ANGRY = "Angry"
    DISGUSTED = "Disgusted"
    SURPRISED = "Surprised"
    FEARFUL = "Fearful"
