#ex6.py
x = "There are %d types of people." % 10 # d specifies that a number of 
#some kind will be inserted into the string"
binary = "binary"
do_not = "don't"
y = "those who know %s and those who %s." % (binary, do_not)

print x
print y

print "I said: %r." % y
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "this is the left side of..."
e = "a string with a right side."

print w + e

#note: Use the %r for debugging, since it displays the "raw" 
# data of the variable, but the others are used for displaying to users.