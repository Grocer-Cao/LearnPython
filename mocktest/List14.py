from mock import Mock

# The mock object
class Foo(object):
    # instance properties
    _fooValue = 123

    def callFoo(self):
        print "Foo:callFoo_"

    def doFoo(self,argValue):
        print "Foo:doFoo:input =", argValue

class Bar(object):
    # instance properties
    _barValue = 456

    def callBar(self):
        pass

    def doBar(self, argValue):
        pass

# create the first mock object
mockFoo = Mock(spec=Foo)
print mockFoo

mockBar = Mock(spec=Bar)
print mockBar

mockFoo.attach_mock(mockBar, 'fooBar')

print mockFoo
print mockFoo._fooValue
print mockFoo.callFoo()

print mockFoo.fooBar
print mockFoo.fooBar._barValue
print mockFoo.fooBar.callBar()
print mockFoo.fooBar.doBar("narf")