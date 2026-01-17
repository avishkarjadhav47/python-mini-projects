import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Listening... Please speak clearly for 5 seconds")
    audio = r.record(source, duration=5)
    text = r.recognize_google(audio)
    print(text)
