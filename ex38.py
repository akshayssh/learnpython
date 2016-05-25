# Doing things to Lists - ex38.py
ten_things = "Apples Oranges Crows Telephone Light Sugar"
#print "The list 'ten_things:", ten_things # unnecessary - this list is parsed and printed on lines 7,8
# print "Number of items in list 'ten_things", len(ten_things) # This will count every single character including spaces
print "Wait there are not 10 things in that list. Let's fix that."

stuff = ten_things.split(' ')
print "Printing the list 'stuff':", stuff # debug only
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) <> 10:
	next_one = more_stuff.pop()
	print "Adding: ", next_one
	stuff.append(next_one)
	print "There are %d items now." % len(stuff)
	
print "There we go: ", stuff
print "Let's do some things with stuff."

print "stuff[1]:\t", stuff[1]
print "stuff[-1]:\t", stuff[-1] # Whoa! fancy
print "stuff.pop():\t ", stuff.pop()
print "' '.join(stuff):\t", ' '.join(stuff) # What? cool!
print "'#'.join(stuff[3:5]):\t", '#'.join(stuff[3:5]) # super stellar!
	