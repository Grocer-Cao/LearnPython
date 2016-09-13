# coding: utf-8
from mock import Mock


class Foo(object):
    # instance properties
    _fooValue = 123

    def callFoo(self):
        print "Foo:callFoo_"

    def doFoo(self, argValue):
        print "Foo:doFoo:input =", argValue


# creating the mock object (without a side effect)
fooObj = Foo()

mockFoo = Mock(return_value=fooObj)
print mockFoo

mockObj = mockFoo()
print mockObj

mockFoo = Mock(return_value=fooObj, side_effect=EnvironmentError)
# 由于上一行Mock中指定了side_effect的值,所以他将覆盖掉return_value
# mockObj = mockFoo()
