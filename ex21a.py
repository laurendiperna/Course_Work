#ex21a.py
# define a function that does simple math
# you can only use one return statement?
# return causes your function to exit and hand back a value
# to its caller, print just returns a string to the console
def simple_math(a, b, c):
	print "ADDING a + b, and then SUBTRACTING c"
	return (a + b) - c
	

#call the function simple_math
#this will not print without a print statement
#result equals the result of your simple_math function when you type in
# 5,6 and7
result = simple_math(5, 6, 7)

print "How did we get", result, "we use the arguments 5, 6 & 7"


