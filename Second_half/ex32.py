#the_count = [1, 2, 3, 4, 5]
#fruits = ['apples', 'oranges', 'pears', 'apricots']
#change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# This first kind of for loop goes through a list
#for number in the_count:
#    print "This is count %d" % number

# same as above
#for fruit in fruits:
#    print "A fruit type is %s." % fruit

# also we can go through mixed lists
# notice we have to use %r since we don't know what's in it
#for i in change:
#    print "I've got %r" % i

# we can also build lists. First start with an empty one.

# then use the range function to do a 0 - 5 count
#for i in range(6):
#    print "Adding %d to the lists." % i
    # append is a function that lists understand
#    elements.append(i)

# now we can print them out too
elements = range(9)
print elements
elements.sort(reverse = True)
print elements