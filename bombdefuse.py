import pyttsx3
speaker = pyttsx3.init() #create a speaker object - has its own namespace
speaker.setProperty('rate', 300)
speaker.say("BOOOOOOOM!")
speaker.runAndWait()