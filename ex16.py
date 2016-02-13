# begin the argv import from the sys
from sys import argv

# set the variables for argv. This always starts with script, which just gives the name of the script.
script, filename = argv

target = open(filename, 'r+')

# print the message that we're going to erase
print "We're going to erase %r." % filename

# print the option to stop. I believe that control-c just makes the script stop
print "If you don't want to erase %r, hit CTRL-C (^C)." % filename

# command to hit return to continue
print "If you don't want that, hit RETURN"

# This asks for teh input with a "?" prompt,
# but doesn't do anything with the response.
# In other words it's just an opportunity to pause
# and give everyone the opportunity to abandon their process.
raw_input("?")

# Honestly, not sure what the 'w' does here. I think
# it's an argument for the open command making the file writable.
# but this loads the file into the variable 'target'
print "Opening the file..."

# This truncates the file, which seems to delete everything after the
# "position" the script is in in the file. By default, that position is character 1.
print "Truncating the file %r. Goodbye!" % filename
target.truncate()


print "Now I am going to ask for three lines."

# This adds three variables through raw_input
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

# this writes the variables to the file, with a "new line" character after each variable
target.write("%s\n%s\n%s" % (line1, line2, line3))

# This closes the file. Not totally sure what that means, but I know you have to do it.
print "And finally, we print and close it."

target.close()
