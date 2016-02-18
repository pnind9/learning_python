print "You enter a dark room with two doors. Do you go through door #1 or door #2?"

door = raw_input("> ")

if door == "1":
    print "There's a giant bear here eating a cheesecake. What do you do?"
    print "1. Take the cake."
    print "2. Scream at the bear."
    print "3. Try to ride the bear."

    bear = raw_input("> ")

    if bear == "1":
        print "The bear eats your face off. Good job!"
    elif bear == "2":
        print "The bear eats your legs off. Good job!"
    elif bear == "3":
        print "WOOO HOOO YOU'RE RIDING A BEAR!!!!"
        print "Where do you want to go now?"
        print "1. Ride the bear into a black hole."
        print "2. Ride out of door one."

        ride = raw_input("> ")

        if ride == "1":
            print "A black hole is a super-dense singularity. You are reduced to your component particles, and so is the bear."
        elif ride == "2":
            print "There is no door number one anymore. All is lost :("
        else:
            print "There are no other options."

    else:
        print "Well, doing %s is probably better. Bear runs away." % bear

elif door == "2":
    print "You stare into the endless abyss at Cthulhu's retina."
    print "1. Blueberries."
    print "2. Yellow Jacket Clothespins."
    print "3. Understanding revolver's yelling melodies."

    insanity = raw_input("> ")

    if insanity == "1" or insanity == "2":
        print "Your body survived powered by a mind of jello. Good job!"
    else:
        print "The insanity rots your eyes into a pool of mush. Good job!"

else:
    print "You stumble around and fall on a knife and die. Good job!"