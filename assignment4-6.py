# Assignment for functions -- assignment4-6.py
in_hours = raw_input("Please enter hours: ")
in_rate = raw_input("Please enter rate per hour: ")
#Check if hours input is valid, throw exception and quit prog
try:
    hours = float(in_hours)
except:
    print("Error in input, please enter valid input for hours!")
    quit()
    
#Check if rate input is valid, throw exception and quit prog
try:
    rate = float(in_rate)
except:
    print("Error in input, please enter valid input for rate!")
    quit()

 # Function definition to compute over time pay
def computepay(h, r):
    return ((40 * r) + (h-40.0) * r * 1.5)

pay = hours * rate
   
if (hours > 40.0):
    pay = computepay(hours, rate)

print pay
