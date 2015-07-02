#ex31b.py

print "You can't decide if you should quit your job so you decide to flip a coin."
print "If the coin is heads, type heads."
print "If the coin is tails, type tails."

coin_flip = raw_input("> ")

if coin_flip == "heads": #you left this as "=" but for an if statement it needs to be "=="
	print "You quit your job. Now your free!"
elif coin_flip == "tails":
	print "You decided to stay. Hmm I guess you like stability."
else:
	print "I know it's never that easy."
	
#you tried having two else: statements and it didn't work, not sure why, maybe 
#because else has to end the block and you can't continue it with another else
#yeah actually it looks like it broke on line 14 where the second else finishes