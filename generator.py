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
	
	get_words()
	append_words()