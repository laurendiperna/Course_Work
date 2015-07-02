#ex16a.py
from sys import argv

script, filename = argv

new_file = open(filename) #create the file object
print new_file.read()     #print out the contents
new_file.close			  #close the file