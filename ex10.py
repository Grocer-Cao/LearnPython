# coding: utf-8

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm spilt\non a line."
backlash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backlash_cat
print fat_cat

# 回车符会回到本行的开头，将本行全部擦除
AAA = "abcdef\r123"

print AAA
