def cheese_and_crackers(cheese_count, boxes_of_craclers):
    print "You have %d cheese!" % cheese_count
    print "you have %d boxes of crackers!" % boxes_of_craclers
    print "Man thats pretty much!"
    print "Get a blanke.\n"


print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

print "OR, we can use variables from our script"
amount_of_cheese = 30
amount_of_crackers = 20

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "Or we do the math in it"
cheese_and_crackers(1+2, 3+4)

print "or we combine both"
cheese_and_crackers(amount_of_cheese + 2, amount_of_crackers + 1)

print "End of Code!"