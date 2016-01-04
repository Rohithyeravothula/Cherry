import pyttsx


class Speak():
	def __init__(text):
		self.text=text
	#def 


e = pyttsx.init()
e.say("Hello Rohith")
e.runAndWait()
