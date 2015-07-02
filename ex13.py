#ex13.py
from sys import argv #import is how you add features (modules)
					 #argv is the "argument variable" it holds
					 #the arguments you pass to the python script

script, first, second, third = argv #this unpacks argv, and assigns
									#it variables

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

fourth = raw_input("add a fourth variable name here: ")
print "Your last variable is:", fourth

# to run this script you have to type python ex13.py (and then three variable 
# names) 