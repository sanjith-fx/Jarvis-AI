import pyttsx3
from config import VOICE_RATE, VOICE_VOLUME

engine = pyttsx3.init()

engine.setProperty("rate", VOICE_RATE)
engine.setProperty("volume", VOICE_VOLUME)


def speak(text):
    print(f"\nJarvis : {text}\n")

    engine.say(text)
    engine.runAndWait()