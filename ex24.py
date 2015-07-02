#ex24.py
# print a statement
print "Let's practice everything."
# if you want to continue a line of code onto the second line use the '\' then
# continue writing on the second line (you don't need to tab the second line).
print 'You\'d need to know \'bout escapes with \\ that do \
\n newline and \t tabs.'

#use triple quotes to write a paragraph, or keep formatting of several lines
poem = """
 \tThe lovely world
 with logic so firmly planted
 cannot discern \n the needs of love
 nor comprehend passion from intuition
 and requires an explanation
 \n\t\twhere there is none.
 """

# print more strings, and between them call the variable 'poem' defined above 
print "--------------"
print poem
print "--------------"
 
# use simple math to assign a variable
five = 10 - 2 + 3 - 6
print "This should be five: %s" % five

# write a function that returns three variables
# you can assign the variables names to the left of the function (see below)
def secret_formula(started):
	jelly_beans = started * 500
 	jars = jelly_beans / 1000
 	crates = jars / 100
 	return jelly_beans, jars, crates
 	
 	
start_point = 10000
# it looks like you can assign your variable to a definition
# 'beans' doesn't have to be 'jelly_beans', because 'jelly_beans
# within the function is just a place holder
beans, jars, crates = secret_formula(start_point)

print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

start_point = start_point / 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d creates." % secret_formula(start_point) 
 