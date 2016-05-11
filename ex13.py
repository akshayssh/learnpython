# Parameters, Unpacking, Variables -- ex13.py
from sys import argv
#argv = raw_input("Enter four strings, first one being ex13.py:\n")

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
fourth = raw_input("What is your fourth variable?")