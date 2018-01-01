import speech_recognition as sr
from time import ctime
import time
import os
import pyttsx
engine = pyttsx.init()
from pyttsx import voice

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='en')
    tts.save("audio.mp3")
    os.system("mpg321 audio.mp3")
 
def recordAudio():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
 
    # Speech recognition using Google Speech Recognition
    data = ""
    try:
        # Uses the default API key
        # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        data = r.recognize_google(audio)
        #print("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
 
    return data
 
def jarvis(data):
    if "how are you" in data:
        engine.say("I am fine")
        engine.runAndWait()
        
        
    if "what is your name" in data:
        engine.say("My name is Jarvis")
        engine.runAndWait()    
 
 
    if "what time is it" in data:
        engine.say(ctime())
        engine.runAndWait()
        
 
 
    if "where is" in data:
        data = data.split("is")
        location = data[1]
        engine.say("Hold on Frank, I will show you where " + location + " is.")
        engine.runAndWait()
        import webbrowser
        #location='Mumbai'
        webbrowser.open("https://www.google.com/maps/place/" + location + "/&amp;")
        
    if "what is " in data or "who is " in data:
       data = data.split("is")
       location = data[1]
       if "your name" not in location:
        engine.say("Hold on Frank, I will find  " + location )
        engine.runAndWait()
        import webbrowser
        #location='Mumbai'
        webbrowser.open("https://www.google.co.in/search?q="+location)
        
    if "run " in  data or "execute" in data:
        engine.say("Executing the program" )
        engine.runAndWait()
        import os
        os.chdir('C:\\Users\\rounayak\\Documents\\Fuso\\OCR\\Round 1\\looper')
        os.system('python "OCR automator.py" --image 0A1637.tif')
        
        
    if "open" in data or "output" in data:
        engine.say("Opening the file" )
        engine.runAndWait()
        import os
        os.chdir('C:\\Users\\rounayak\\Documents\\Fuso\\OCR\\Round 1\\looper')
        os.system('Extraction2.csv')
        
        
        
        
       


    
    if "stop" in data:
        return 0
    
    
    
        
 
        #os.system("chromium-browser https://www.google.nl/maps/place/" + location + "/&amp;")
 
# initialization
time.sleep(2)
engine.say("Hi Frank, what can I do for you?")
engine.runAndWait()
 
while 1:
    data = recordAudio()
    m=jarvis(data)
    
    if m==0:
        break