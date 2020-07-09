import pyttsx3 # pyttsx3 : python text to speech version 3
import datetime
# import pywin32 # pywin32 : python windows 32 bit
import pythoncom
# list1=["chetan","yamini","harshita","rajesh", "aman"]
engine=pyttsx3.init("sapi5") #sapi5: speech instruction mode 5
voice=engine.getProperty("voices")
# print(voice[0].id)
engine.setProperty('voice',voice[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# num=int(input("enter your attandance:"))
# speak(f"answered by {list1[num-1]}")



# def wishme():
#     arts = int(datetime.datetime.now().hour)
#     speak("my name is johnson  and speed is 1TB")
#     speak("how can i assist you lucky")
#     if (arts >= 0 and arts <= 12):
#         speak("good morning")
#     elif (arts > 12 and arts <= 18):
#         speak("good afternoon")
#     elif (arts > 6 and arts < 21):
#         speak("good evening")
#     else:
#         speak("good night")


# speak("how can i assist you ")
# wishme()

# str1=input("Enter your text:")
# speak(str1)


