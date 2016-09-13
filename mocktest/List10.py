# coding: utf-8
from mock import Mock


class Foo(object):
    # instance properties
    _fooValue = 123

    def callFoo(self):
        pass

    def doFoo(self):
        pass


# create the mock object
mockFoo = Mock(spec=Foo)
print mockFoo

mockFoo.callFoo()
mockFoo.callFoo.assert_called_once_with()

# 报错,由于assert_called_once_with检测时要求该方法只被执行了一次
# AssertionError: Expected 'callFoo' to be called once. Called 2 times.
# mockFoo.callFoo()
# mockFoo.callFoo.assert_called_once_with()
