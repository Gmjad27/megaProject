import speech_recognition as sr

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio)
            print(f"You: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand.")
            return None
        except sr.RequestError:
            print("Error connecting to Google Speech Recognition.")
            return None




# def takeCommand():
#     r = speech_recognition.Recognizer()
#     with speech_recognition.Microphone() as source:
#         print("Listening......")
#         r.adjust_for_ambient_noise(source)
#         # print(query)
#         # r.pause_threshold = 3
#         # r.energy_threshold = 4000
#         audio = r.listen(source, 0, 1)

#     try:
#         print("Understanding..")
#         query = r.recognize_google(audio, language='en-in')
#         print(f"You Said: {query}\n")

#     except Exception as e:
#         print("Say that again.")
#         return "None"
#     return query


