# coding: utf-8

# 在每行 print 后面加了个逗号,这样的话 print 就不会输出新
# 行符而结束这一行跑到下一行去了。
print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight)

# raw_input()与input(),这两个函数均能接收字符串,但 raw_input()
#   直接读取控制台的输入（任何类型的输入它都可以接收）。而对于
#   input() ，它希望能够读取一个合法的 python 表达式，即你输入字
#   符串的时候必须使用引号将它括起来，否则它会引发一个 SyntaxError 。
# raw_input() 将所有输入作为字符串看待，返回字符串类型。而
#   input() 在对待纯数字输入时具有自己的特性，它返回所输入的数字
#   的类型（ int, float ）；同时在例子 1 知道，input() 可接受合
#   法的 python 表达式，举例：input( 1 + 3 ) 会返回 int 型的 4 。

print "What is you name?",
name = input()
print "So, your name is %r" % name

# 注意，不管是raw_input()还是input()它们都是直接从控制台读取数据，
# 所以不可以写成 raw_input(173)
