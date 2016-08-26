# coding: utf-8


# this one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)


# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)


# this just takes one argument
def print_one(arg1):
    print "arg1: %r" % arg1


# this one takes no aruments
def print_none():
    print "I got nothin'."


print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()

# +++++++++++++++++++附加题++++++++++++++++++++
# 1、函数定义是以def开始的
# 2、函数名称是由字符和下划线 _ 组成的
# 3、函数名称不用紧跟着括号也可以，但最好紧跟着
# 4、括号里可以包含参数也可以不包含
# 5、同一函数中参数名称不可以相同
# 6、参数结束后跟着的是“):”
# 7、紧跟着函数定义的代码使用了4个空格的缩进
# 8、函数结束的位置取消了缩进
# ---------------------------------------------
