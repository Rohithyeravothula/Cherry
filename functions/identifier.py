import os


class Main:
	def __init__(self, command):
		self.homepath     = os.getcwd()
		prefixwords_path  = self.homepath + "/wordbase/prefixwords.txt"
		mainwords_path    = self.homepath + "/wordbase/mainwords.txt"
		postfixwords_path = self.homepath + "/wordbase/postfixwords.txt" 
		mainwordsmapping_path  = self.homepath + "/wordbase/mainwordsmapping.txt"

		f=open(prefixwords_path)
		self.prefixwords = f.read().split("\n")
		f.close()

		f=open(mainwords_path)
		self.mainwords = f.read().split("\n")
		f.close()

		f=open(postfixwords_path)
		self.postfixwords = f.read().split("\n")
		f.close()

		f=open(mainwordsmapping_path)
		words = f.read().split("\n")
		self.mainwordsmapping = {}
		for word in words:
			key, value = word.split(':')
			key = key.strip()
			value = value.strip()
			self.mainwordsmapping[key] = value

		self.prefixcommand = "Null"
		self.maincommand = "Null"
		self.postfixcommand = "Null"

		self.prefixcommand = command.split(" ")[0]
		self.maincommand = command.split(" ")[1]
		self.postfixcommand = command[len(self.prefixcommand)+1+len(self.maincommand)+1:len(command)]

		if self.prefixcommand not in self.prefixwords:
			self.maincommand = self.prefixcommand
			self.prefixcommand = "Null"
		
		if self.maincommand not in self.mainwords:
			self.maincommand = "Null"

		self.command = "Null"

		if self.maincommand != "Null":
			self.command = self.mainwordsmapping[self.maincommand]

	def identifiedcommand(self):
		return self.command



if __name__ == '__main__':
	test = Main("open chrome")
	print test.mainwordsmapping
	print test.identifiedcommand()
	#print test.mainwordsmapping
	#print test.prefixcommand, test.maincommand, test.postfixcommand
	
	
