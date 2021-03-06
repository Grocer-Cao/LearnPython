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


# create the mock object
mockFoo = Mock(spec=Foo)
print mockFoo

# assert_called_with
# 用于检测:1、是否方法是否被调用 2、调用时传入参数是否是期望值
# 注意:它只可以用于检测类,而不可以用于检测对象
mockFoo.doFoo("narf")
mockFoo.doFoo.assert_called_with("narf")

s = "oscar"
mockFoo.doFoo(s)
mockFoo.doFoo.assert_called_with("oscar")

d = 123456
mockFoo.doFoo(d)
mockFoo.doFoo.assert_called_with(123456)

# 报错,原因是调用时传入参数与期望值(assert...后跟的)不符
# mockFoo.doFoo("zort")
# mockFoo.doFoo.assert_called_with("narf")
