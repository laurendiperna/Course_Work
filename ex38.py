#ex38.py
ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there are not 10 things in that list. Let's fix that."

#ten_things.split(' ') translated into what Python does is split(ten_things, ' ')
#Call split on ten things, converting the words into strings
# and (not sure here) and uses the whitespace as separator
stuff = ten_things.split(' ')
# I think this: stuff = ten_things.split() is the same as the code line above
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
	next_one = more_stuff.pop()
	print "Adding: ", next_one
	#stuff.append(next_one): Python does as append(stuff, next_one)
	#Calls append on stuff and next_one, so appends next_one to stuff
	stuff.append(next_one)
	print "There are %d items now." % len(stuff)
	
print "There we go: " , stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1] #whoa! fancy
#stuff.pop(): Python does as pop(stuff)
#
print stuff.pop()
#''.join(stuff): Python does join('', stuff)
#Calls join on stuff and uses ' ' as the separator between string elements in stuff
print ' '.join(stuff) #what? cool!
#'#'.join(stuff[3:5]): Python does join('#',stuff[3:5])
#calls join on stuff elements 3 and 4 and uses # as the separator
print '#'.join(stuff[3:5]) #super stellar!