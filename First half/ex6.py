# An initial statement with an internal variable for types of people
x = "There are %d types of people." % 10

# a couple of variables...
binary = "binary"
do_not = "don't"

# An additional string with two string formatting operators
y = "Those who know %s and those who %s." % (binary, do_not)

# Printing two variable strings
print x
print y 

# Re-printing those two lines, but using two different string formatting operators. 
# The %r operator uses repr() which "reproduces" the content as a string. This also adds single quotes.
print "I said: %r." % x

# This uses the %s operator, which is Str(), which conveys a string. This doesn't add any quotes, so you have to add them manually.
print "I also said: '%s'." % y 

# Variable declarations...
hilarious = False

# This variable contains a formatting operator. 
joke_evaluation = "Isn't that joke so funny?! %r"

# This prints a string that includes a formatting operator, and passes in a value to the operator of the "hilarious" variable
print joke_evaluation % hilarious

w = "This is the left side of..."
e = " a string with a right side."

# print two strings, using the "+"
print w + e
print w,e 
