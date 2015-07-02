#ex19.py
# This function takes the arguments 'cheese_count' and 'boxes_of_crackers' and
# inserts them into the three sentences, with the values assign in line 10
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Get a blanket.\n'"
	
# line 11 is what gives you the numbers for the lines above, without it the above
# do not print
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

# lines 15-16 assign values to the variables for line 19, and reprints the function
# define in line 4
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

# This calls the function defined in line 4
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# same thing but you're doing sums to define the variables
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

# same thing but you are adding numbers to variables
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
