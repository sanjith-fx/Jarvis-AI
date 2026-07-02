from voice.listen import listen
from voice.speak import speak

from commands.command_handler import execute


def run():

    speak("Hello Sir. Jarvis Online.")

    while True:

        command = listen()

        if command == "":
            continue

        if "stop" in command or "exit" in command:

            speak("Goodbye Sir.")

            break

        execute(command, speak)


if __name__ == "__main__":

    run()