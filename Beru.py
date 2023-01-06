import datetime
import pyttsx3
import speech_recognition as sr
import pyaudio
#this code is to get voice 
beru=pyttsx3.init()
voices=beru.getProperty('voices')
beru.setProperty('voice',voices[0].id)
beru.setProperty('rate',150)
def speak(text):
    '''this function is will convert String to audio'''
    beru.say(text)
    beru.runAndWait()
def take():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listining...")
        r.energy_threshold=300
        r.threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing.")
        query=r.recognize_google(audio, language="en-in")
    except Exception as e:
        speak("I cant understand")
        query=input("Tell me how can i assist u: ")
    return query.lower()
def Greetings():
    '''this function will greet as soon as program run'''
    hour,minute=int(datetime.datetime.now().hour),int(datetime.datetime.now().minute)
    if hour>=0 and hour<12:
        speak("Good morning master.")
        sign="Am"
    elif hour>=12 and hour<=17:
        speak("Good afternoon master.")
        sign="Pm"
    else:
        speak("Good Evining master.")
        sign="Pm"
    time,minute=str(abs(12-hour)),str(minute)
    if time=="0":
        time="12"
    speak("It's"+time+minute+sign+"I hope u are doing good")
Introduction="I'm Beru. an AI created by master Saksham Arora"
if __name__=="__main__":
    Greetings()
    while True:
        command=take()
        if "go back" in command:
            break
        elif command=="none":
            continue
        else:
            speak(command)
