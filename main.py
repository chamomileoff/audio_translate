import speech_recognition as sr
import pyttsx3
from translate import Translator

translator = Translator(from_lang='Russian', to_lang='English')
engine = pyttsx3.init()
r = sr.Recognizer()


# talk function
def talk(text):
    engine.say(text)
    engine.runAndWait()


talk(".")


# translator function
def listen():
    with sr.Microphone() as source:
        audio = r.listen(source)
        text = r.recognize_google(audio, language="ru-RU")
        if text:
            talk(translator.translate(text))


# running function
if __name__ == '__main__':
    listen()
