#Assignment 3.1 -- assignment3-1.py

inp = raw_input("Please enter a score between 0.0 and 1.0: ")
try:
    score = float(inp)
except:
    print"Invalid entry, please try again."
    quit()

if ( score < 0.0 or score > 1.0 ):
    print "Error, the value is out of range [0.0, 1.0]"
    quit()

# Calculating the grade if the input is in acceptable range
if(score >= 0.9):
    print "Grade A"
elif(score >= 0.8):
    print "Grade B"
elif (score >= 0.7):
    print "Grade C"
elif(score >= 0.6):
    print "Grade D"
else:
    print "Grade F"