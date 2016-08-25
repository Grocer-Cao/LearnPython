# coding: utf-8
# Here's some new strange stuff, remember type it exactly.
days = "Mon Tue Wed Thu Fri Sat Sun"
months = "\nJan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print "Here are the days:", days
print "Here are the months", months

# """ 是一种符号，所以中间不能加空格 '''也是一种符号，两者等效
print """
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
"""

print "Here are the months %r" % months

print "Here are the days:", days
print "Here are the days:" + days
