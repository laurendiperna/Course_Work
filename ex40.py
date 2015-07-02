#ex40.py

class Song(object):

	def __init__(self, lyrics): #I don't understand the two variable
		self.lyrics = lyrics

		
	def sing_me_a_song(self):
		for line in self.lyrics:
			print line
			

			
happy_bday = Song(["Happy birthday to you", 
				   "I don't want to get sued", 
				   "So I'll stop right there"])
				   
bulls_on_parade = Song(["They rally around tha family",
						"With pockets full of shells"])
						
green_day = Song(["I am one of those",
			"melodramatic fools",
			"neurotic to the bone"])						
						
happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

print "This one is all you: "
green_day.sing_me_a_song()

print #########

new_lyrics = "It's your thing, do what you wanna do!"

thing = Song(new_lyrics)
thing.new_lyrics

						