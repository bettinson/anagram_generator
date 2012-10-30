class generator:
	def get_words():		#Grabs the words
		global words
		global letters
		words = raw_input("input the letters\n")
		letters = []	

	def append_words():		#Puts the words into an array
		i = 0
		for word in words:
			letters.append(word)
			print letters[i]
			i = i + 1	
	
	def get_dictionary():
		path = "/usr/share/dict/words"
	
	def gen_words():
		temp = ""
		length = len(letters)
		i = 0
		for i in range(len(letters) - 1):
			temp = letters[i] + letters[i + 1]
			print temp
			i = i + 1
			
	get_words()
	append_words()
	gen_words()