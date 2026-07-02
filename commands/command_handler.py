import datetime

from browser.browser import open_youtube
from browser.browser import youtube_search
from browser.browser import youtube_play

from ai.brain import ask_ai


current_site = None


def execute(command, speak):

    global current_site

    if "time" in command:

        current_time = datetime.datetime.now().strftime("%I:%M %p")

        speak(f"The time is {current_time}")

    elif "open youtube" in command:

        open_youtube()

        current_site = "youtube"

        speak("Opening YouTube.")

    elif "play" in command:

        video = command.replace("play", "")
        video = video.replace("on youtube", "")
        video = video.strip()

        if current_site == "youtube":

            youtube_play(video)

            speak(f"Playing {video} on YouTube.")

        else:

            speak("Please open YouTube first, sir.")    

    elif "search" in command:

        query = command.replace("search", "")
        query = query.replace("on youtube", "")
        query = query.strip()

        if current_site == "youtube":

            youtube_search(query)

            speak(f"Searching {query} on YouTube.")

        else:

            speak(ask_ai(query))

    else:

        speak(ask_ai(command))