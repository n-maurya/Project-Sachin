import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voices', voices[0].id)


def speak(audio):
     engine.say(audio)
     engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
          speak("Good Morning!")
    elif hour>=12 and hour<18:
          speak("Good Afternoon!")
    else:
          speak("Good Evening!")
    speak("I am Sachin. Please tell me how may I help you")


def takeCommand():
     #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
         print("Listening...")
         r.energy_threshold = 300
         r.pause_threshold = 1
         audio = r.listen(source)
    
    try:
         print("Recognizing...")
         query = r.recognize_google(audio, language='en-in')
         print(f"User said: {query}\n")
         
    except Exception as e:
         print(e)
         print("Say that again please...")
         return "None"
    return query


def listenForKeyword():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        while True:
            print("Listening for keyword 'Sachin'...")
            r.energy_threshold = 300
            r.pause_threshold = 0.5
            audio = r.listen(source)
            
            try:
                query = r.recognize_google(audio, language='en-in').lower()
                if 'sachin' in query:
                    speak("Yes Sir")
                    return
            except Exception as e:
                print(e)
                continue


if __name__ == "__main__":
    wishMe()
    while True:
        listenForKeyword()
        query = takeCommand().lower()

        #   logic to executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            search_query = query.replace('open youtube and search for', '').strip()
            if search_query:
                url = f"https://www.youtube.com/results?search_query={search_query}"
                webbrowser.open(url)
            else:
                webbrowser.open("https://www.youtube.com")

        elif 'open google' in query:
            search_query = query.replace('open google and search for', '').strip()
            if search_query:
                url = f"https://www.google.com/search?q={search_query}"
                webbrowser.open(url)
            else:
                webbrowser.open("https://www.google.com")
        
        elif 'open facebook' in query:
            webbrowser.open("facebook.com")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = 'E:\\MUSIC\\Song'
            songs = os.listdir(music_dir)
            random_song = random.choice(songs)
            # print(songs)
            os.startfile(os.path.join(music_dir, random_song))

        elif 'the time' in query:
             strTime = datetime.datetime.now().strftime("%H:%M:%S")
             print("Time: ",strTime)
             speak(f"Sir, the time is {strTime}")
        
        elif 'quit' in query or 'exit' in query or 'bye' in query:
             speak("Goodbye! Have a nice day!")
             break
             
  


    #  speak("Hello Sir, I am your personal assistant. How may I help you?")