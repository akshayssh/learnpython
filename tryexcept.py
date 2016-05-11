# Try and except exercise: tryexcept.py

hours = 20
rate = raw_input("Enter rate: ")
try:
    rate = int(rate)
except:
    print "Please enter numeric input."

