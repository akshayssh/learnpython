# assignment5-2.py
# Author: Akshay Heblikar Date: 06-21-2015
#Initialize variables
i = 0;
arr_in = []
largest = None
smallest = None
# Keep doing this until user enters 'done'
while True:
    inp = raw_input("Please enter a number: ")
    if (inp == 'done'):
        print "Done!"
        largest = max(arr_in)
        smallest = min(arr_in)
        print "Maximum", largest
        print "Minimum", smallest
        break
    else:
        try:
            #print i #---debug only
            try: #try to convert to an integer
                arr_in.append(int(inp))
                #print arr_in[i] #---debug only
                i = i + 1
            except: # try to convert to a floating point
                arr_in.append(float(inp))
                #print  arr_in[i] #---debug only
                i = i + 1
                continue
        except: # throw an error to the user with some examples and continue to run the program
            print "Please enter a valid number; like 0, 1, 2, 3.9, 99.87,..."
            continue
