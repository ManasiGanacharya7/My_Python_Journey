#Install external module and use it

import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')       #getting details of current voice
engine.setProperty('voice', voices[0].id)

engine.say("I will speak this text")
engine.say("My name is Mansi And I will complete the whole python course and it's my promise, mark my words")
engine.say("Nann Hesar Mansi Anta , Maaza Naav Mansi ahe ani mazhya Maanzharach naav Kittu ahe teaaj uundir ghari anlela")

engine.runAndWait()

