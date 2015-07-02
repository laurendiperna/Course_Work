#ex29.py
people = 20
cats = 30
dogs = 15

#the indentation is used to start and end the if statement
#the if statement checks if the inequality or statement is true or false
#if it is true it prints the statment below it.
if people < cats:
	print "Too many cats! The world is doomed!"

if people > cats:
	print "Not many cats! The world is saved!"
	
if people < dogs:
	print "The world is drooled on!"
	
if people > dogs:
	print "The world is dry!"
	
dogs += 5

if people >= dogs:
	print "People are greater than or equal to dogs."
	
if people <= dogs:
	print "People are less than or equal to dogs."
	
if people == dogs:
	print "People are dogs."