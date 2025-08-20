import speech_recognition as sr
import os
import webbrowser
import datetime
import pyttsx3
import sys
import random
import subprocess

def chat(query):
    try:
        result = subprocess.run(
            ["ollama", "run", "llama3.2"],
            input=query,
            text=True,
            capture_output=True
        )

        response = result.stdout.strip()

        print("AI:\n", response)
        return response if response else "Sorry, no response."

    except Exception as e:
        print("Error running Ollama:", e)
        return "Sorry, I couldn't process that."


def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language = 'en-in') #language can be hindi or other
            print(f"User said: {query}\n")
            return query
        except Exception as e:
            return "Sorry there is an error!"

if __name__ == "__main__":
    say("Welcome to AI Assistant! How may I help you?")
    while True:
        print("Listening...")
        query = takeCommand()
        sites = [["youtube","https://www.youtube.com/"],["wikipedia","https://www.wikipedia.com/"],["google","https://www.google.com/"],["twitter","https://x.com/"],["chat GPT","https://chatgpt.com/"],["spotify","https://open.spotify.com/"]]
        for site in sites:
            if f'open {site[0]}'.lower() in query.lower():
                say(f"Opening {site[0]}...")
                webbrowser.open(site[1])
        if "open music" in query.lower():
            musicPath = "C:\\Users\\sandi\\Music"
            songs = [f for f in os.listdir(musicPath) if f.lower() != "desktop.ini"]
            if songs:
                song = random.choice(songs)
                print(f"Opening {song}...")
                os.startfile(os.path.join(musicPath, song))
            else:
                print("No songs found.")
        elif "the time" in query.lower():
            strfTime = datetime.datetime.now().strftime("%H:%M:%S")
            say(f"The time is {strfTime}")
        elif "open camera or facetime" in query.lower():
            #os.system(f"")
            #paste your link
            pass
        elif "quit" in query:
            say("Goodbye!")
            sys.exit()
        elif 'use artificial intelligence' in query.lower():
            user_request = query.lower().replace("use artificial intelligence", "").strip()
            if not user_request:
                say("Sure, what would you like to ask?")
                user_request = takeCommand()
            response = chat(user_request)  # full response, no line limit
            say(response)

