import webbrowser
import datetime
import pyttsx3
from gtts import gTTS
from googletrans import Translator

engine=pyttsx3.init('sapi5')
voice=engine.getProperty('voices')
engine.setProperty('voice',voice[0].id)

def speak(talk):
    engine.say(talk)
    engine.runAndWait()

# speak("hello this chetan")

import requests
import json
import speech_recognition as sr
import wikipedia
import os

def speakcmd():
    demo=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening..........")
        demo.adjust_for_ambient_noise(source,duration=1)
        demo.pause_threshold=1
        audio=demo.listen(source)
        # print(audio)

    try:
        get_text=demo.recognize_google(audio,language="en-in")
        print(f"user said:{get_text}")
    except Exception as e:
        print(e)
        print("something is wrong, so please say again.......")
        return "something is wrong, so please say again......."

    return get_text
listen=speakcmd().lower()
speak(listen)

# def Speaks(str):
#     from win32com.client import Dispatch
#     demo=Dispatch("SAPI.Spvoice")
#     demo.Speaks(str)

# speak("news for todays.....lets begin")
#
# url="http://newsapi.org/v2/top-headlines?country=in&apiKey=59987112eeb547d1a18f5b2df5109d55"
# content=requests.get(url).text
# speak("wait.... we are fetching data")
# print(content)
# news_dict=json.loads(content)     # json # javascript object notation
#
# print(news_dict)
# arts=news_dict['articles']
# print(arts)

# for article in arts:
#     print(article['title'])
#     speak(article['title'])
#     speak("move to the next news")

if 'wikipedia' in listen:
    print("Searching in Wikipedia.....")
    set_text=listen.replace('wikipedia','')
    result=wikipedia.summary(set_text,sentences=2)
    print(f"according to wikipedia{result}")
    speak(result)
elif 'open' in listen:
    set_text=listen.replace('open','')
    print(set_text)
    get_search=set_text.replace('','')
    print(get_search)
    link='https://www.'
    extn='.com'
    search_url=link+get_search+extn
    webbrowser.open(search_url)

elif'newspaper' in listen:

    speak("news for todays.....lets begin")

    url = "http://newsapi.org/v2/top-headlines?country=in&apiKey=59987112eeb547d1a18f5b2df5109d55"
    content = requests.get(url).text
    speak("wait.... we are fetching data")
    # print(content)
    news_dict = json.loads(content)  # json # javascript object notation

    # print(news_dict)
    arts = news_dict['articles']
    print(arts)

    for article in arts:
        print(article['title'])
        speak(article['title'])
        print("news in detail")
        print(article['description'])
        speak(article['description'])
        speak('do you want to listen next news?')
        print('do you want to listen next news?')
        var=speakcmd()
        if 'next news'in var:
            speak('moving to next news')
            continue
        elif 'no' in var:
            speak("thank you!")
            break
        else:
            speak("sorry your voice is not clear!")
            

elif 'the time' in listen:
    str1=datetime.datetime.now().strftime("%H:%M:%S")
    print(str1)
    speak(str1)




