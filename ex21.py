#ex21.py

# the function add calls two arguments 'a' and 'b', then we
# print out what the function is doing, then we return the addition
# of a and b
# you can return anything that you can put to the right of an '='
def add(a, b):
	print "ADDING %d + %d" % (a, b)
	return a + b
	
def subtract(a, b):
	print "SUBTRACTING %d - %d" % (a, b)
	return a - b

def multiply(a, b):
	print "MULTIPLYING %d * %d" % (a, b)
	return a * b
	
def divide(a, b):
	print "DIVIDING %d * %d" % (a, b)
	return a / b
	
print "Let's do some math with just functions!"

# below I call the functions listed above and assign values
# to the arguments
age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

# A puzzle for the extra credit, type it in anyway
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"

#by_hand does the same calculation as 'what', but with everything written out
# notice the ordering for the subtract function by hand
by_hand = (height -(weight * (iq / 2))) + age

print by_hand

#now let's do the reverse, first write an equation by hand then use functions:
simple_by_hand = (age * height) - iq
# you will also get the print statements for subtract and multiply when you use them
by_function = subtract(multiply(age, height), iq)

print "does",simple_by_hand," equal ", by_function, "?"