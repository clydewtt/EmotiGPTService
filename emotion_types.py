"""This class contains all the emotions specified from FaceAPI"""

from strenum import StrEnum


class Emotions(StrEnum):
    NEUTRAL = "neutral"
    HAPPY = "happy"
    SAD = "sad"
    ANGRY = "angry"
    DISGUSTED = "disgusted"
    SURPRISED = "surprised"
    FEARFUL = "fearful"
