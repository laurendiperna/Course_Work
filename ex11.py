#ex11.py
print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So you're %r old, %r tall and %r heavy." % (age, height, weight)


#note if you put a comma at the end of each print line, it prevents print from
#ending the line with a newline character before moving to the next line.

#without the commas you get:
#How old are you?
#27
#How tall are you?
#5'3"
#How much do you weigh?
#130
#So you're '27' old, '5\'3"' tall and '130' heavy.

#with the commas you get
#How old are you? 27
#How tall are you? 5'3"
#How much do you weigh? 130
#So you're '27' old, '5\'3"' tall and '130' heavy.

#the height has to have the single quote escaped otherwise it would break the string