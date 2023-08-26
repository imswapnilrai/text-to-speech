import pyttsx3
import speech_recognition

def speechrecognition():
    recognizer=speech_recognition.Recognizer()
    while True:
        try:
            with speech_recognition.Microphone() as mic:
                
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio= recognizer.listen(mic)
                
                text=recognizer.recognize_google(audio)
                text=text.lower()
                
                print(f"Recognized {text}")
        except speech_recognition.UnknownValueError():
            recognizer=speech_recognition.Recognizer()
            
def textrecognition():
    text_speech =pyttsx3.init()
    text = input()
    text_speech.say(text)
    text_speech.runAndWait()
    
n=int(input('1 or 2'))
if (n==1):
    speechrecognition()
elif(n==2):
    textrecognition()
    
    

        

