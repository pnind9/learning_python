from sys import exit

# set a couple of global variables that influence the progression of the game.
clothes = False
tries = 5

# tryhard function manages the countdown of wrong moves until the aliens eat you.
# It calls global tries so it can manage a countdown. It takes the next function needed
# as an argument so it can pass the player back to the right spot.
def tryhard(next_function):
    global tries
    tries -= 1
    if tries > 0:
        print "You can hear the aliens getting closer, they're only %r minutes behind you. You'd better hurry up!" % tries
        next_function()
    elif tries == 0:
        print "Aliens found you, you are dead now, soon to be alien poop."
        exit()

# med_bay provides the choices from the medical bay room.
def med_bay():
    print "\nWhat are you going to do now?"
    choice = raw_input("> ")

    if "crate" in choice:
        print "You open the crate."
        crate()

    elif "button" in choice and clothes == False:
        print "You can't go out there, you're naked!"
        tryhard(med_bay)

    elif "button" in choice and clothes == True:
        print "That's a good idea, now that you have clothes on."
        print "You push the button and the door wooshes open to reveal a corridor."
        print "You step into the corridor and the door closes behind you."
        corridor_description()

    elif "where" in choice or "Where" in choice:
        print "You're in the medical bay."
        tryhard(med_bay)

    else:
        print "I have no idea what that means. Remember, there's a crate, and the door with an open button."
        tryhard(med_bay)

# crate function tells the options for when you're opening the crate, depending on state.
# if you've already put the clothes on, you'll be looking at an empty crate.
def crate():
    global clothes
    if clothes == False:
        print "You see your clothes folded up in a pile."
        print "Do you want to put them on?"

        choice = raw_input("> ")

        print choice

        if choice == "yes" or choice == "Yes":
            clothes = True
            print "You put on  your old clothes. They smell like stinky alien sweat."
            print "I think some gross sweaty alien was wearing them."
            print "You close the crate."
            med_bay()

        elif choice == "no" or choice == "No":
            print "Oh, you want to stay naked?"
            print "Maybe I wasn't clear. You're naked."
            tryhard(crate)

        else:
            print "Crate function broke."

    elif clothes == True:
        print "The crate is empty."
    else:
        print "Shit's broken."

def corridor_description():
    print """
    You're in a short, wide corridor. There's a door to your left with a
    window into space and a big red button next to it.

    At the other end of the corridor you see someone in a lab coat, looks
    like a doctor. She's facing away from you, concentrating on a panel on the wall.
    The words and symbols on the panel don't look like any language you've
    ever seen before.

    In the far right corner is another storage crate, and on the right-hand wall is
    another door with a green button, it looks like the door you just passed through.
    """
    corridor_action()

def corridor_action():
    print "What do you want to do?"
    choice = raw_input("> ")



print """
You wake up abruptly. You're laying on a bed, naked,
in what looks like a medical bay. Looking out of the
window you can see the rings of saturn... you're in space!

There's a storage crate in one corner of the room. There's one
door, with a but green activation button next to it.
    """
med_bay()
