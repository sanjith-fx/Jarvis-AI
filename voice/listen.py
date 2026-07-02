import speech_recognition as sr


def listen():

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:

        recognizer.adjust_for_ambient_noise(source)

        print("Listening...")

        audio = recognizer.listen(source)

    try:

        command = recognizer.recognize_google(audio)

        print("You :", command)

        return command.lower()

    except:

        return ""