#ex25.py
def break_words(stuff):
	"""This function will break up words for us."""
	words = stuff.split(' ')
	return words
	
#for this function to work you have to assign 'words' as a variable equal to
#break_words(stuff) where stuff is a sentence otherwise it will sort the letters in 
#your words
#everything in """ """ will appear as your documentation if you use 'help(ex25) in python
def sort_words(words):
	"""Sorts the words."""
	return sorted(words)
	
#when you pop one of the words off it actually removes it from the set of strings defined
#by words
#pop actually removes the specified item from a list
def print_first_word(words):
	"""Prints the first word after popping it off."""
	word = words.pop(0)
	print word
	
def print_last_word(words):
	"""Prints the last word after popping it off."""
	word =  words.pop(-1)
	print word
	
def sort_sentence(sentence):
	"""Takes in a full sentence and returns the sorted words."""
	words = break_words(sentence)
	return sort_words(words)
	
def print_first_and_last(sentence):
	"""Prints the first and last words of the sentence."""
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)

def print_first_and_last_sorted(sentence):
	"""Sorts the words then prints the first and last one."""
	words = sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words)