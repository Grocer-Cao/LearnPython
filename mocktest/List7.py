# coding: utf-8

from mock import Mock


# The mock object
class Foo(object):
    # instance properties
    _fooValue = 123

    def callFoo(self):
        print "Foo:callFoo_"

    def doFoo(self, argValue):
        print "Foo:doFoo:input =", argValue


# creating the mock object(with a side effect)
fooObj = Foo()
# 一旦mockFoo到达了列表的末尾，调用将引发StopIteration 错误
fooList = [665, 666, 667]
mockFoo = Mock(return_value=fooObj, side_effect=fooList)

fooTest = mockFoo()
print fooTest

fooTest = mockFoo()
print fooTest

fooTest = mockFoo()
print fooTest

# 报错,StopIteration
# fooTest = mockFoo()
# print fooTest
