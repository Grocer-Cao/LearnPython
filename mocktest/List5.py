# coding: utf-8
from mock import Mock

class Foo(object):
    _fooValue = 123

    def callFoo(self):
        print "Foo:callFoo_"

    def doFoo(self, argValue):
        print "Foo:doFoo:input =",argValue

fooObj = Foo()

mockFoo = Mock(return_value=fooObj)
print mockFoo

# 由于return_value是一个类,所以得到的mockFoo也是一个类,
# 所以应该要实例化再使用
mockObj = mockFoo()

print mockObj

print mockObj._fooValue

mockObj.callFoo()

mockObj.doFoo("narf")
