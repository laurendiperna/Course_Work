#ex19a.py
# The function sandwich has two arguments "jelly_type" which has to be
# a string and "number_of_slices" which has to be a number
# if you used %r instead of %s and %d you could use whatever type you wanted
# for the arguments
# it outputs two print statements one that takes the first argument
# and the second that takes the second argument
def sandwich(jelly_type, number_of_slices):
	print "I like this kind of %s" % jelly_type
	print "between %d slices of bread" % number_of_slices

# here we call the function sandwich and enter in a string "strawberry jam"
# and an number '2'), it will then run through the function defined above
sandwich('strawberry jam', 2)

# here we assign the variables for the function, then print those variables in a 
# different order then they are taken in the definition
number_of_slices = 10
jelly_type = 'blackberry jam'
print "%d slices with only a little %s is a terrible idea " % (number_of_slices,jelly_type)

# here we call the function, but with the arguments that are given above 'blackberry jam'
# and '10'
sandwich(jelly_type, number_of_slices)

# here we do sums within the arguments
sandwich('peanut butter' + ' jelly time', 5 + 10)

# here we take the arguments defined above (lines 19 - 20) and add a string fro the first
# and a number for the second
sandwich(jelly_type + ' peanut_butter', number_of_slices + 100)

print ""
# here we ask for raw input, BUT all raw_inputs are strings so you have to convert
# the number of slices (aka raw_slices) to an int with 'int()'
raw_jam = raw_input('what jam do you like?')
raw_slices = int(raw_input('and how many slices do you want?'))

print 'so you would say the following is true?'
sandwich(raw_jam, raw_slices)