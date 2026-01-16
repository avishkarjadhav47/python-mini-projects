import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("..Initialised..")
    audio = r.record(source, duration=5)
    text = r.recognize_google(audio)
    print(text)
