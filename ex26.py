#ex26.py
def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words) 

def print_first_word(words): #added in a colon
    """Prints the first word after popping it off."""
    word = words.pop(0) #changed from 'poop' to 'pop'
    print word

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1) #missing a ')' added that in
    print word

def sort_sentence(sentence): #I'm not sure you can enter a sentence as your arg
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence) #I would add ' ' to sentence to make this work
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)


print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""


print "--------------"
print poem
print "--------------"

five = 10 - 2 + 2 - 5 #fixed the math
print "This should be five: %d" % five # changed %s to %d

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000 #changed \ to /
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point) #changed == to =, and - to _

print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)
#changed 'jeans' to 'beans'

start_point = start_point / 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)
#crabapples are not defined, changed to crates
#added ')' in and fixed start_pont to start_point"

sentence = "All god \t things come to those who weight." #there are spelling mistakes but
#that won't break the code
#I don't know how to remove the \t from being sorted

import ex25

words = ex25.break_words(sentence)
sorted_words = ex25.sort_words(words)

#there needs to be a line here where you import ex25.py
#or maybe not
#from ex25 import *

print_first_word(words)
print_last_word(words)
print_first_word(sorted_words) #removed . before print
print_last_word(sorted_words)
sorted_words = ex25.sort_sentence(sentence)
print sorted_words #added a 't' to prin

print_first_and_last(sentence) #added in a 'f'

print_first_and_last_sorted(sentence) #removed the indent, added in 'nd' to and, and t 
#to senence

