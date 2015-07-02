#34.py

from sys import exit
#exit is a modulus that lets you abort a program and produce an error
#if you have exit(0) it's a good exit and no error gets printed, if you type exit(1)
#there will be an error, exit(2) exit(100) display other error types.

def gold_room():
	print "This room is full of gold. How much do you take?"
	
	choice = raw_input("> ")
	if "0" in choice or "1" in choice:
		how_much = int(choice)
	else:
		dead("Man, learn to type a number.")
	
	if how_much < 50:
		print "Nice, you're not greedy, you win!"
		exit(0) #changed this from exit(0) to exit(1) to see what happens
				#i didn't see anything with exit(1)
	else:
		dead("You greedy bastard!")
		
		
def bear_room():
	print "There is a bear here."
	print "The bear has a bunch of honey."
	print "The fat bear is in front of another door."
	print "How are you going to move the bear?"
	bear_moved = False
	
	while True:
		choice = raw_input("> ")
		
		if choice == "take honey":
			dead("The bear looks at you then slaps your face off.")
		elif choice == "taunt bear" and not bear_moved:
			print "The bear has moved from the door. You can go through it now."
			bear_moved = True #this now sets bear_moved equal to True so if you type
							  #'taunt bear' again the below statement becomes true
		elif choice == "taunt bear" and bear_moved:
			dead("the bear gets pissed off and chews you leg off.")
		elif choice == "open door" and bear_moved:
			gold_room()
		else:
			print "I got no idea what that means."
			
def cthulhu_room():
	print "Here you see the great evil Cthulhu."
	print "He, it, whatever stare at you and you go insane."
	print "Do you flee for you life or eat your head?"
	
	choice = raw_input("> ")
	
	if "flee" in choice:
		start()
	elif "head" in choice:
		dead("Well that was tasty!")
	else:
		cthulhu_room()
		
		
def dead(why):
	print why, "Good job!"
	exit(0)
	
def start():
	print "You are in a dark room."
	print "There is a door to your right and left."
	print "Which one do you take?"
	
	choice = raw_input("> ")
	
	if choice == "left":
		bear_room()
	elif choice == "right":
		cthulhu_room()
	else:
		dead("you stumble around the room until you starve.")
		
start() #this is the first thing typing 'python ex34.py' you will see that's why you get
		#'you are in a dark room' and then the code proceeds into the bear_room function
		#or the cthulhu_room function
		
#I didn't figure out what using exit(2) does or if you can tell that a 2 was used 
#instead of 1, I get that it means an abnormal exit but I don't see any output
#that is different for exit(2) as opposed to exit(0)