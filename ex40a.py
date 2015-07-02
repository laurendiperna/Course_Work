#ex40a.py

# this goes in ex40a.py

#def apple():
	#print "I AM APPLES!"
	
#tangerine = "Living reflection of a dream"	

#when you run this in python, after importing 'ex40a' it seems like you are saying
#look in this file "ex40a" and then the dot '.' says look for the variable that follows
#or the definition, then execute that definition on ex40a

#in the case of the dictionary the key is a string and the syntax is [key]. In the case
# of a module, the key is an identifier and the syntax is .key
#classes are like module, you can think about a module as a specialized dictionary that
#can store Python code so you can access it with the . operator. Python also has another
#construct that serves a similar purpose called a class. A class is a way to take a grouping
#functions and data and place them inside a container so you can access them with
#the dot operator

#the trick is understanding the difference between local variable and attribute
#to pass a variable to a class you have to have the variable defined in the class
#or call the class outside the class definition as shown belwo

class MyStuff(object):
	def __init__(self):
		self.tangerine = "And now a thousand years between"
		self.lyrics2 = "lallalal"
		
	def apple(self):
		print "I AM CLASSY APPLES!"
		
	lyric_variable = "do dah, do dah"
		
#objects are like import
#if a class is like a "mini-module", then there has to be a similar concept to 
#import but for classes. That concept is called instantiate, which means 'create'

class Song(object):
	def __init__(self, lyrics):
		self.lyrics = lyrics
		
	def sing_me_a_song(self):
		for line in self.lyrics:
			print line
			
bulls_on_parade = Song(["They rally around tha family",
						"With pockets full of shells"])

bulls_on_parade.sing_me_a_song()



test = MyStuff()

