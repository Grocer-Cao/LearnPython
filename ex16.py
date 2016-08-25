# coding: utf-8
from sys import argv

script, filename = argv
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."
raw_input("?")
print "Opening the file..."
#关于打开文件时的关键字，说明如下：
#   r  只可读           r+ 可读可写，覆盖写，若不存在报错
#   w  只可写，覆盖写   w+ 可读可写，覆盖写，若不存在创建
#   a  只可写，附加写   a+ 可读可写，附加写，如不存在创建
target = open(filename, 'w')
print "Truncating the file. Goodbye!"
# 如果用了 'w' 打开，则truncate()就不是必须的了，
# 它将会自动擦除并重写
# target.truncate()
print "Now I'm going to ask you for three lines."
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")
print "I'm going to write these to the file."
# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")
target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")

print "And finally, we close it."
target.close()
