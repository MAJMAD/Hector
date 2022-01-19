import pyttsx3 as sp
import speech_recognition as sr
import cv2
import threading
import requests
from bs4 import BeautifulSoup
import csv



class AIIPP:

    def __init__(self, name = "", friends = [], family = [], interests = [], thoughts = [], mood = "", topics = {}):
        self.name = name
        self.ears = sr.Microphone()
        self.voice = sp.init()
        self.eyes = cv2.VideoCapture(0)
        self.friends = friends
        self.family = family
        self.interests = interests
        self.brain = [] #todo this will doubtfully remain as a list
        self.thoughts = thoughts
        self.mood = mood
        self.topics = topics
        self.start(self)
        
    def start():
        Hector = self
        cv2.imshow(Hector.see())
        Hector.introduce_self()
        message = Hector.listen()
    # process message
    Hector.speak("I Like you")

    info = Hector.ask_question("Ava")
    if info == "* is a friend":
        Hector.friends.append(info)

    def listen(self, echo = 1):
        with sr.Microphone() as source:
            r = sr.Recognizer()
            self.voice.say("I'm listening")
            self.voice.runAndWait()
            audio = r.listen(source)
            message = r.recognize_google(audio)
            if echo == 1:
                self.repeat(message)
            return message

    def repeat(self, speech):
        self.voice.say("You said : {}".format(speech))
        self.voice.runAndWait()

    def speak(self, speech):
        self.voice.say(speech)
        self.voice.runAndWait()

    def see(self):
        #thread this so once called it can continue to run alongside other apps
        ret, sight = self.eyes.read()
        return sight

    def introduce_self(self):
        self.speak("Hello, I am {}".format(self.name))

    def ask_question(self, topic):
        self.speak("Tell me about {}".format(topic))
        return self.listen(0)

    def print_message(self, message):
        print(message)

    def update_dictionary(self, dictionary, key, value):
        dictionary[key] = value
