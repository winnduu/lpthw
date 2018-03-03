count = [1, 2, 3, 4, 5, 6]
hair = ['brown', 'blond', 'red', 'green']
mixed = [1, 'test', 2, 'lululul', 3, 'testing']
fillme = []

for number in count:
    print "numbers are: %s" % number

for color in hair:
    print "Haircolor is: %s" % color

for value in mixed:
    print "value is: %r" % value

for i in range(1, 10):
    print "adding %r to the list" % i
    fillme.append(i)
print(fillme)

