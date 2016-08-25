#coding: utf-8
age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weigh? ")
print "So, you're %r old, %r tall and %r heavy." % (
age, height, weight)

# 命令行中输入 python -m pydoc raw_input 可以用于查看
#  raw_input 的功能介绍