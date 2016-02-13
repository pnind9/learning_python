from sys import argv

script, first, second, third = argv
prompt = '))))))) '

print "Please enter your %s" % first,
first_val = raw_input(prompt)
print "Ok, now please enter your %s" % second,
second_val = raw_input(prompt)
print "Last one, please enter your %s" % third,
third_val = raw_input(prompt)


print """
Ok, so your %s is %s, and your %s is %s, and as far as I know your %s is %s."  
""" % (first, first_val, second, second_val, third, third_val)
