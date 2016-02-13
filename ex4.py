# how many cars do we have to work with?
cars =  100

# How many people can fit into a car?
space_in_a_car = 4.0

# How many people want to drive? 
drivers = 30

# How many people need a ride?
passengers = 90

# Based on how many drivers there are, how many cars will remain undriven?
cars_not_driven = cars - drivers

# How many cars will be driven?
cars_driven = drivers

# What is our total capacity for passengers?
carpool_capacity = cars_driven * space_in_a_car

# What's the average number of people per car?
average_passengers_per_car = passengers / cars_driven

# What is the total number of people that will be traveling?
total_number_of_people = drivers + passengers


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
print "We will have a total of", total_number_of_people, "riding today."

