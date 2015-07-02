#ex16.py
from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w') #this overwrite the file I think and lets you
							 #write over it.

print "Truncating the file. Goodbye!"
target.truncate() #yup not sure what truncate does

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

#the stuff below just writes in the lines above into your file
#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")
target.write("%s\n%s\n%s\n" % (line1,line2,line3)) #do the above in one line

print "And finally, we close it."
target.close()