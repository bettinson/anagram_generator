solution = []
letters = []
path = open("/usr/share/dict/words" , "r")

class generator:
	def get_words():		#Grabs the words
		global words
		words = raw_input("input the letters\n")
			
	def append_words():		#Puts the words into an array
		i = 0
		for word in words:
			letters.append(word)
			i = i + 1	
	
	def gen_words():		#Generates the words
		temp = ""
		length = len(letters)
		i = 0
		for i in range(len(letters) - 1):
			if letters[i] != "a":
				print letters[i]
			else:
				print "_"
			i = i + 1
			
	get_words()
	append_words()
	gen_words()