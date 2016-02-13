name = 'Ix'
age = 40 # not a lie
height = 76 # inches
height_in_cm = height * 2.54
weight = 223.0 # POUNDS
weight_in_stone = weight / 14.0
weight_in_kg = weight * 0.453592
eyes = 'Blue'
teeth = "White-ish"
hair = "Salt & pepper"

print "Let's talk about %s." % name
print "He's %d inches tall, which is %d centimeters." % (height, height_in_cm)
print "He's %f pounds heavy, which is %f stone, or %f Kg." % (weight, weight_in_stone, weight_in_kg)
print "Actually, that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d and %d I get %d." % (age, height, weight, age + height + weight)