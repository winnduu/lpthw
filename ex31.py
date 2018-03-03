print "You come into a complete dark room with two doors. Do you take Door1 or Door2?"

door = raw_input("> ")

if door == "1":
    print "You See a Bear eating a cake. What do you do?" 
    print "1. Steal and eat the cake" 
    print "2. Scream at the bear like fucking hell" 

    bear = raw_input("> ")

    if bear == "1":
        print "The bear eats your face!"

    elif bear == "2":
        print "The bear eats you legs!"

    else:
        print "Yeah, %s is probably the best idea!" % bear


elif door == "2":
    print "You stare into the endless abyss of god"
    print "1. Blueberries"
    print "2. Yellow jacket cloth"
    print "3. Understanding resolvers yelling melody" 

    insanity = raw_input("> ")

    if insanity == "1" or insanity == "2":
        print "Your body survives healthy" 
    else:
        print "Your body is dead." 

else:
    print "You stumble into a knife an die. Well played." 


