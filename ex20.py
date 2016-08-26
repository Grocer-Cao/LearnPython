# coding: utf-8
from sys import argv

script, input_file = argv


def print_all(f):
    print f.read()


# 关于f.seek(0)
# file.seek()方法标准格式是：seek(offset,whence=0)
# offset：开始的偏移量，也就是代表需要移动偏移的字节数
# whence：给offset参数一个定义，表示要从哪个位置开始偏
# 移；0代表从文件开头开始算起，1代表从当前位置开始算起，
# 2代表从文件末尾算起。默认为0
def rewind(f):
    f.seek(0)


def print_a_line(line_count, f):
    # print之后加逗号可以避免输出回车
    print line_count, f.readline(),


current_file = open(input_file)
print "First let's print the whole file:\n"

print_all(current_file)
print "Now let's rewind, kind of like a tape."

# 这一步的的目的是回到文件的起始位置
rewind(current_file)
print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
