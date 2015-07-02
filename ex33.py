#ex33.py

i = 0
numbers = []

while i < 6:
	print "At the top i is %d" % i
	numbers.append(i) #this appends numbers into your list
	
	i = i + 1
	print "Numbers now: ", numbers #this prints out your list elements adding one at a time
	print "At the bottom i is %d" % i
	
print "the numbers: "

#the for loop doesn't print out until the while loop is done
for num in numbers:
	print num