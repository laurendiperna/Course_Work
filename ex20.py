#ex20.py
from sys import argv

script, input_file = argv

# the function print_all takes in a file that has been opened
# and prints the entire file by reading the file
# read() reads at most size bytes, and returns a string
def print_all(f):
	print f.read()
	
# the rewind function applies 'seek' to your file, seek allows you to specify
# what byte you would like to start at, so in this case we are starting at the 
# beginning of the file (the first byte)
def rewind(f):
	f.seek(0)

# the print_a_line function list the line you are on and then reads that line
def print_a_line(line_count, f):
	print line_count, f.readline()

# current_file is connected to you input_file with the reading attribute
current_file = open(input_file)

# I can't figure out with the \n doesn't actually create a new line
print "First let's print the whole file:\n"

# here you call the function 'print_all' and apply it to the open input_file
# the function then reads and prints out the entire file
print_all(current_file)

print "Now let's rewind, kind of like a tape."

#here you call the function 'rewind' and apply it to your open input_file
# the function starts the file at the first byte
rewind(current_file)

print "Let's print three lines:"


# assigns variable current_line to 1
current_line = 1
# calls the function 'print_a_line' prints the 'current_line' and then reads the line 
print_a_line(current_line, current_file)

# because you have already read the first line the next time this function is called
# it reads the second line, current_line does not effect which line you read
# you can check this if you switch the '1' below to '2'
current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

# += adds another value with the variable's value 
# and assigns the new value to the variable.
# you can text this out in python 'x=3; x += 4; print x"