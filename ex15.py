#Reading Files --ex15.py

from sys import argv

#how to unpack argv
script, filename = argv

#open the file
txt = open(filename)

#display the file name and read it
print "Here is your file %r:" % filename
print txt.read()

#Be courteous, clean up after yourself!
txt.close()

#Ask for file name again with a prompt
print "Type the filename again:"
file_again = raw_input("> ")


#open the file again
txt_again = open(file_again)

#read and display contents of the file again.
print txt_again.read()

txt_again.close()
