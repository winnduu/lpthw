from sys import exit


def gold_room():
    print "This room is full of gold. How much do you take?"
    next = raw_input("> ")
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("Man, learn to type numbers!")

    if how_much < 50:
        print "Nice, youre not greedy, you win!"
        exit(0)
    else:
        dead("You greedy bastard!")


def bear_room():
    print "There is a bear here"
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"
    bear_moved = False

    while True:
        next = raw_input("> ")

        if next == "take honey":
            print "bear fucks your face up"
        elif next == "taunt bear" and not bear_moved:
            print "The bear has moved from the door. You can go through it now"
            bear_moved = True
        elif next == "taunt bear" and bear_moved:
            dead("The bear gets pissed")
        elif next == "open door" and bear_moved:
            gold_room()
        else:
            print "i got no idea what you mean."


def cthulhu_room():
    print "Here you see the great evil Ctulhu."
    print "He, it, whatever stares at you and you go insane."
    print "Do you flee for your life, or eat your head?"
    next = raw_input("> ")

    if "flee" in next:
        start()
    elif "head" in next:
        dead("Well, dat was tasty")
    else:
        cthulhu_room()


def dead(why):
    print why, "good job!"
    exit(0)

def start():
    print "you are in a dark room"
    print "there is a door to your right and left"
    print "which one do you take?"

    next = raw_input("> ")

    if next == "left":
        bear_room()
    elif next == "right":
        cthulhu_room()
    else:
        print "You stumble around and starve to death."


start()