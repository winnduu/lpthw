i = 0
numbers = []

print "how many numbers do you want to fill in your list?"
maximum = int(raw_input("> "))
while (i < maximum):
    print "top: i = %r" % i
    numbers.append(i)
    i = i + 1
    print "bottom: i = %r" % i

print numbers