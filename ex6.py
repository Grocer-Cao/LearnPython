# coding: utf-8
# 给字符串变量（常量？）x赋值
x = "There are %d types of people." % 10
# 同上
binary = "binary"
# 同上
do_not = "don't"
# 同上，字符串包含字符串两次
y = "Those who know %s and those who %s." % (binary, do_not)
# 输出
print x
# 输出
print y
# %r输出 关键在于它会将x单独加引号
print "I said: %r." % x
# %s输出 只有手动加引号是才有引号
print "I also said: '%s'." % y
# 布尔型变量赋值
hilarious = False
# 字符串赋初值
joke_evaluation = "Isn't that joke so funny?! %r"
# 字符串组合输出，字符串包含字符串
print joke_evaluation % hilarious
# 字符串赋初值
w = "This is the left side of..."
e = "a string with a right side."
# 字符串连接，字符串包含字符串
print w + e
