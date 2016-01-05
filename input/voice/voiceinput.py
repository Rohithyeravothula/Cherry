import speech_recognition as sr

class voiceinput:
	def __init__(self):
		self.name = "Voice input processor"
		print self.name
	
	def get_input(self):
		r = sr.Recognizer()
		with sr.Microphone() as source:
			print("Say something!")
			audio = r.listen(source)
		return r.recognize_google(audio)





if __name__ == '__main__':
	test = voiceinput()
	print test.get_input()