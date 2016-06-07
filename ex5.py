# Exercise 5: More Vairables and Printing --ex5.py
name = "Akshay H"
age = 29 # not a lie
height = 68 # inches
weight = 198 #lbs
eyes = 'Brown'
teeth = 'White'
hair = 'Black'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds, heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the cofffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)

height_cm = height * 2.54
weight_kg = weight * 0.453592

print "%s's height in centimeters is %r cms" % (name, height_cm)
print "%s's weight in kilograms is %r kgs" % (name, weight_kg)