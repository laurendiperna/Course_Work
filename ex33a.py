#ex33a.py


#range = raw_input('> ')

def make_list(endpoint, increment): #I'm not sure if range needs to be ''
	i = 0
	numbers = []
	
	while i < endpoint:
		print "At the top i is %d" % i
		numbers.append(i) #this appends numbers into your list
	
		i = i + increment
		print "Numbers now: ", numbers #this prints out your list elements adding one at a time
		print "At the bottom i is %d" % i
	

#make_list(10, 2) #this will just spit out if you type in 'import ex33a' into python



def for_loop_list(endpoint):
	numbers = []
	for i in range(endpoint):
		print "At the top i is %d" % i
		numbers.append(i) #this appends numbers into your list
	
		#i = i + increment
		print "Numbers now: ", numbers #this prints out your list elements adding one at a time
		print "At the bottom i is %d" % i
	 

#print "the numbers: "

#the for loop doesn't print out until the while loop is done
#for num in numbers:
	#print num
	
#k first to use a definition you have to run python, then you have
#to import the script 'from xxx.py import *' that imports everything
#otherwise when you run something you have to use xxx.function

#that fixed that problem but it doesn't seem like I can have the for
#loop in the script, because numbers isn't defined, which doesn't
#make sense because it's created in the while loop

#if you just use import ex33a (once in python) you have to use ex33a.make_list(x)