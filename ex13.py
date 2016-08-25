# coding: utf-8
from sys import argv
script, first, second= argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second

age = raw_input("How old are you? ")
print "%r" % age

# 必须在控制台中运行，不可以在IDE环境下运行，
# 因为它需要获取参数变量。