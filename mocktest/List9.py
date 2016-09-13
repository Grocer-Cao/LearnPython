# coding: utf-8
from mock import Mock


# The mock object
class Foo(object):
    # instance properties
    _fooValue = 123

    def callFoo(self):
        pass

    def doFoo(self, argValue):
        pass

fooObj = Foo()

# create the mock object
mockFoo = Mock(return_value=fooObj)
print mockFoo

# assert_called_with
# 用于检测:1、是否方法是否被调用 2、调用时传入参数是否是期望值
# 注意:它只可以用于检测类,而不可以用于检测对象
mockFoo.callFoo()
mockFoo.callFoo.assert_called_with()

# 报错,因为callFoo不支持任何输入
mockFoo.callFoo("Hello")
mockFoo.callFoo.assert_called_with()

