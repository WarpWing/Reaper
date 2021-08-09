import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import time
import subprocess
import os 
import sys
import json
import requests
import platform 
import socket,json,psutil,logging






# Voice Engine Init
engine=pyttsx3.init('espeak')
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[0]id')


#Small TTS Function
def speak(text):
    engine.say(text)
    engine.runAndWait()

#Greet Function 
def greeting():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")


def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as src:
        print("Listening for commands")
        audio=r.listen(src)

        try:
            input=r.recognize_google(audio,language='en-in')
            print(f"User said:{input}\n")

        except Exception as e:
            speak("Apologies, please speak up")
            return "None"
        return input

speak("Loading up Reaper")
greeting()


if __name__=='__main__':


    while True:
        speak("Awaiting command.")
        statement = takeCommand().lower()
        if statement==0: #This begins the command array
            continue

        if "goodbye" in statement or "terminate" in statement:
            speak('Shutting down Reaper')
            break

        elif 'test' in statement:
            speak("Test command")
            time.sleep(2)
           
            



time.sleep(2)





    



