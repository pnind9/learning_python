# call in the string from the command line
from sys import argv

# define the variables from the command line
script, input_file = argv


# create a function called "print_all" with argument "f",
# which prints the results of running the read action on "f"
# which is the placeholder argument
def print_all(f):
    print f.read(),
    print "\n"


# This is a function that rewinds the playhead using the "seek" action
# it seems when a script is utilizing a file there is a sense of
# place: like a position of the playhead, or a spot for the cursor
def rewind(f):
    f.seek(0)


# creating a function with arguments that include line_count and f
# Then printing the value of line_count (a number) and then uses the
# readline() method to read the line where the "playhead" is
def print_a_line(line_count, f):
    print "\t",
    print line_count, f.readline()



#def list_file(f):
#    print f.list



# opening a file to create a file object, and naming it "current_file"
current_file = open(input_file)


print "First, let's print the whole file: \n"


# calling the "print all" function, and passing the "current_file" object as
# an argument. This funtion will run the "read()" method on the
# file object and print the result
print_all(current_file)

print "Now let's rewind, kind of like a tape. \n"


# call the "rewind" function, passing the current_file object as an arguiment
# Rewind function accepts the named file object and uses the "seek()" method
# to move the scripts position in the file to byte 0
rewind(current_file)


print "Let's print three lines: \n"


# assign an int value of 1 to current_line. Call function print_a_line with arguments
# being current_line value and current_file object. When you run "readline()" it
# includes the \n at the end of each line, so that naturally moves the "playhead"
# to the beginning of the following line.

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

rewind(current_file)
