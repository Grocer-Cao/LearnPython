# coding: utf-8
# 导入获取命令参数的包
from sys import argv

# 设定需要输入几个命令参数
script, filename = argv
# 打开一个文件，获取到文件的指针
txt = open(filename)
# 输出信息
print "Here's your file %r:" % filename
# 读取文件并打印出来
print txt.read()
#关闭文件
txt.close()

# 输出信息
#print "Type the filename again:"
# 再次读取文件名
#file_again = raw_input("> ")
# 再次打开文件
#txt_again = open(file_again)
# 再次读取文件
#print txt_again.read()
#关闭文件
#txt_again.close()

#肯定是使用argv的方式获取文件名称的方式更好，因为它可以自动补全