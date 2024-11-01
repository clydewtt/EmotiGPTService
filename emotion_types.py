"""This class contains all the emotions specified from FaceAPI"""

from enum import Enum


class Emotions(Enum):
    NEUTRAL = "neutral"
    HAPPY = "happy"
    SAD = "sad"
    ANGRY = "angry"
    DISGUSTED = "disgusted"
    SURPRISED = "surprised"
    FEARFUL = "fearful"
