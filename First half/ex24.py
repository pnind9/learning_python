print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print "----------------"
print poem
print "----------------"

five = 10 - 2 + 3 - 6
print "This should be five: %s" % five


def secret_formula(started):
    beans = started * 500
    jars = beans / 1000
    crates = jars / 100
    return beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point)

print "With a starting point of %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

# start_point = start_point / 10

print "We can also do it this way:"
start_point = float(raw_input("Starting point >"))
print start_point

print "We'd have %f beans, %f jars, and %f crates." % secret_formula(start_point)