# coding: utf-8
def add_and_multiply(x, y):
    addition = x + y
    multiple = multiply(x, y)
    return (addition, multiple)


def multiply(x, y):
    # 因为此处的操作导致测试不通过,但实际add_and_multiply()函数
    # 以及它的测试用例并没有做任何修改，罪魁祸首是multiply()函数
    # 引起的，所以我们应该把 multiply()函数mock掉。
    return x * y + 3
