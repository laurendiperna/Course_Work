#ex5.py
name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74. * 2.54 #inches converted to cm
weight = 180. * 0.453592 #lbs converted to kg
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %r." % name
print "He's %r centimeters tall." %height
print "He's %d kilograms heavy." %weight
print "Actually that's not too heavy."
print "He's got %r eyes and %r hair." % (eyes, hair)
print "His teeth are usually %r depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "if I add %d, %d, and %d I get %d." % (age, height, weight,
age + height + weight)

#notes, when you replace %s (which makes your variable strings) with
# %r, it applies repr() instead of str() to your variables, and thereby
# represents your objects (it keeps the information about your variable, 
# rather then just converting it to a string)