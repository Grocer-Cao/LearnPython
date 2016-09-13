# coding: utf-8
from mock import Mock


class Foo(object):
    _fooValue = 123

    def callFoo(self):
        print "Foo:callFoo_"

    def doFoo(self, argValue):
        print "Foo:doFoo:imput = ", argValue


mockFoo = Mock(spec=Foo)

print mockFoo

print mockFoo._fooValue

print mockFoo.callFoo()

# nothing happens, which is fine
# 无论属性方法是否有功能代码，调用mock的该属性方法时也什么都不会做
mockFoo.callFoo()

# print mockFoo._fooBar
#
# mockFoo.callFoobar()
