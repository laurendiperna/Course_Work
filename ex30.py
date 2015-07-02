#ex30.py
people = 30
cars = 40
trucks = 15

#pay attention to the colon operator and make sure it's at the end of any else
#make sure the colon is after the inequality, not just the elif (no don't "elif:")
#python will stop after the first if statement that it sees is true
if cars > people:
	print "We should take the cars."
elif cars < people:
	print "We should not take the cars."
else:
	print "We can't decide."
	
if trucks > cars or trucks != cars:
	print "That's too many trucks."
elif trucks < cars:
	print "Maybe we could take the trucks."
else:
	print "We still can't decide."
	
if people > trucks:
	print "Alright, let's just take the trucks."
else:
	print "Fine, let's stay home then."