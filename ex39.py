states = {'Oregon': 'OR',
          'Florida': 'FL',
          'California': 'CA',
          'New York': 'NY',
          'Michigan': 'MI'
}

cities = {'CA': 'San Franzisco',
          'MI': 'Detroit',
          'FL': 'Jacksonville'
}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

#Some Cities
print '-' * 10
print "NY State has:", cities['NY']
print "OR State has: ", cities['OR']

#Some States
print "michigans abbreviation is: ", states['Michigan']
print "Floridas abbreviation is: ", states['Florida']

#Combined
print "-" * 10
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

#Every abbreviation

for abbrev, city in states.items():
    print "%s is abbreviated %s" % (abbrev, city)

#print every city
for abbrev, city in cities.items():
    print "%s has the city %s" % (abbrev, city)

#now both at the same time
print '-' * 10
for state, abbrev in states.items():
    print "%s state is abbreviated %s and has the city %s" % (state, abbrev, cities[abbrev])

#Exceptions
print '-' * 10
state = states.get('Texas', None)
if not state:
    print "Sorry, no Texas"

#default value
city = cities.get('TX', 'Does not exist!')
print "The City for the state 'TX' is: %s" % city