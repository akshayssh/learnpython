## Dictionaries --ex39.py

# create a mapping of state abbreviation

states  = {
			'Oregon': 'OR',
			'Florida': 'FL',
			'California': 'CA',
			'New York': 'NY',
			'Michigan': 'MI'
			}
			
## create a basic set of states and some cities in them

cities = {
		'CA': 'San Jose',
		'MI': 'Detroit',
		'FL': 'Jacksonville'
		}
		
# add some more cities

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

## print out some cities
print '-' * 30
print "NY State has:", cities['NY']
print "OR state has:", cities['OR']

#print some states
print '-' * 30
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

# do it by using the state then cities dict
print '-' * 30
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

# print every state abbreviation
print '-' * 30
for state, abbrev in states.items():
	print "%s is abbreviated %s" %(state, abbrev)

#print every city in state
print '-' * 30
for abbrev, city in cities.items():
		print "%s has the city %s" % (abbrev, city)
		
# now do both at same time
print '-' * 30
for state, abbrev in states.items():
	print "%s state is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev])
	
print '-' * 30
#safely get an abbreviation by state that might not be there
state = states.get('Texas')

if not state:
	print "Sorry, no Texas."
	
# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print "The city for the satte 'TX' is %s" % city