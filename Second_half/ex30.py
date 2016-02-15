people = 30
cars = 40
trucks = 30


if cars > people:
    print "There are %r more cars than people. we should take a car." % (cars - people)
elif cars < people:
    print "We should walk."
else:
    print "WALKING AND CAR DEADLOCK."

if trucks > cars:
    print "That's too many trucks."
elif trucks < cars:
    print "Maybe we could take the trucks"
else:
    print "I ain't sure about them trucks."

if people > trucks:
    print "Alright, let's just take the trucks."
else:
    print "Fine, let's stay home then."