import random
from time import gmtime, strftime

roll_summary = []

def dice_roll(dice_sides, dice_number):
    for x in xrange(dice_number):
        dnum = (x + 1)
        roll = random.randrange(1, (dice_sides + 1))
        kind = ""

        print "Rolling %d sided dice #%d: %d" % (dice_sides, dnum, roll),

        roll_summary.append("\n\t%r" % roll)

        if dice_sides == 20 and roll == 20:
            kind = "CRITICAL HIT!!"
        elif dice_sides == 20 and roll == 1:
            kind = "MAJOR BOTCH!!!"
        elif dice_sides >= roll:
            print "",
        else:
            print "Broken crit & botch"

        print "\t%s" % kind
        roll_summary.append("\t%s" % kind)


def record_roll():
    timestamp = strftime("%m-%d %H:%M", gmtime())
    with open('rolls.txt', 'a') as roll_record:
        roll_record.write("\nRolling %r at %r" % (roll_description, timestamp))
        roll_record.write(" ".join(str(r) for r in roll_summary))
        roll_record.write("\n")


dice_sides = input("How many sides? -- > ")
dice_number = input("How many dice? -- > ")
roll_description = "%dD%d" % (dice_number, dice_sides)
print "Rolling %s" % roll_description
dice_roll(dice_sides, dice_number)
record_roll()

