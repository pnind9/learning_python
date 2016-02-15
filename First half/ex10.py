tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."
food = "\t20 cups"
fish = "\t7 fish"
catnip = "\t3 bags"
grass = "\t1 sq. ft."

fat_cat = """
I'll do a list:
\t* Cat food:%s
\t* Fishies:%s
\t* Catnip:%s\n\t* Grass:%s
""" % (food, fish, catnip, grass)


print tabby_cat
print persian_cat
print backslash_cat
print fat_cat