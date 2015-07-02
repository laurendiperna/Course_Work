#ex15.py
from sys import argv

script, filename = argv #ask yourself what you need the user to input
						#before they hit enter to run the file
						
txt = open(filename) #this creates the file object, but does not open the file
					 #when you don't specify the mode it defaults to read ('r')
					 
print "Here's your file %r: " % filename
print txt.read() #this reads the entire file, no parameters specified

txt.close()		 #closes the file to free up any system resources the open file
				 #may use

print "Type the filename again: "
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read() #have python read the file. the ".' allows you to give
					   #a file a command (function or method) and parameters 
					   #(this one has no parameters)
txt_again.close()
				   
#to open a file directly in python
# > python
# >>> f = open('ex15_sample.txt','r') #this opens the file/makes a connection
# >>> print f.read()
# make sure not to type f = open('ex15_sample.txt','w')
# because then you can overwrite whatever you had in your script