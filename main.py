import pyaudio
import pyttsx3
import speech_recognition as sr
import pywhatkit
import datetime
import random
import wikipedia



listener=sr.Recognizer()
engine=pyttsx3.init()
engine.setProperty("voice","french")
engine.setProperty("rate",170)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def greetme():
    current_hour=int(datetime.datetime.now().hour)
    if 0 <= current_hour<12:
        talk("bonjour scof mon createur")
    if 12<= current_hour<=18:
        talk("bon apres midi scof")
    if current_hour>18 and current_hour != 0:
        talk("bonsoir")

voice=engine.getProperty("voices")
engine.setProperty("voice",voice[1].id)
greetme()
engine.say("comment vas tu mon scofield")
engine.runAndWait()

def alexa_command():
    with sr.Microphone() as source:
        print("lire............")
        listener.pause_threshold = 5
        voice=listener.listen(source)
        command=listener.recognize_google(voice,language="fr-FR")
        command=command.lower
        print(command)
        if "alexa" in command:
            command=command.replace("alexa", "")
            print(command)
        return command

    def run_alexa():
        command=alexa_command()
        if "musique" in command:
            song=command.replace("musique","")
            talk("musique en cours.....")
            pywhatkit.playonyt(song)
        elif "heure" in command:
            time=datetime.datetime.now().strftime("%H:%H")
            talk("il est actuelment :",time)
        elif "qui est" in command:
            person=command.replace("qui est","")
            wikipedia.set_lang("fr")
        elif "sortir" in command:
            talk("desoler je sius souffrante")
        elif "es-tu en couple"in command:
            talk("oui")
        else:
            talk()

    

if __name__=="__main__":
    pass