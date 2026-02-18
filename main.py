import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pywhatkit
import os
import sys

# Initialize engine
engine = pyttsx3.init()
engine.setProperty('rate', 175)

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except:
        return ""

def wish_me():
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good morning")
    elif hour < 18:
        speak("Good afternoon")
    else:
        speak("Good evening")
    speak("I am your voice assistant. How can I help you?")

def execute_command(command):

    if "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {time}")

    elif "wikipedia" in command:
        speak("Searching Wikipedia")
        query = command.replace("wikipedia", "")
        result = wikipedia.summary(query, sentences=2)
        speak(result)

    elif "open youtube" in command:
        speak("Opening YouTube")
        pywhatkit.open_web("https://youtube.com")

    elif "open google" in command:
        speak("Opening Google")
        pywhatkit.open_web("https://google.com")

    elif "search" in command:
        speak("Searching")
        pywhatkit.search(command.replace("search", ""))

    elif "play" in command:
        song = command.replace("play", "")
        speak(f"Playing {song}")
        pywhatkit.playonyt(song)

    elif "open vscode" in command:
        speak("Opening Visual Studio Code")
        os.system("code")

    elif "shutdown" in command:
        speak("Shutting down system")
        os.system("shutdown now")

    elif "exit" in command or "stop" in command:
        speak("Goodbye")
        sys.exit()

    else:
        speak("Sorry, I don't understand that yet")

# Main loop
wish_me()
while True:
    cmd = listen()
    if cmd:
        execute_command(cmd)
