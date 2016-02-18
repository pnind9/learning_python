def count_numb(count, increm):
    i = 0
    numbers = []

    while i < count:
        print "At the top i is %d" % i
        numbers.append(i)

        i += increm
        print "Numbers now: ", numbers
        print "At the bottom i is %d \n" % i

    print "The numbers: "

    for num in numbers:
        print num


print "Let's try it like this:"
numba = input("Max number >> ")
incra = input("increment  >> ")

count_numb(numba, incra)