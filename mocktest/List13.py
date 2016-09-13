from mock import Mock, call


# The mock specification
class Foo(object):
    _fooValue = 123

    def callFoo(self):
        pass

    def doFoo(self, argValue):
        pass


# create the mock object
mockFoo = Mock(spec=Foo)
print mockFoo
# returns <Mock spec='Foo' id='507120'>

mockFoo.callFoo()
mockFoo.doFoo("narf")
mockFoo.doFoo("zort")

fooCalls = [call.callFoo(), call.dooFoo("narf"), call.doFoo("zort")]

mockFoo.assert_has_calls(fooCalls)
# AssertionError: Calls not found.
# Expected: [call.callFoo(), call.dooFoo('narf'), call.doFoo('zort')]
# Actual: [call.callFoo(), call.doFoo('narf'), call.doFoo('zort')]

fooCalls = [call.callFoo(), call.dooFoo("narf"), call.doFoo("zort")]
mockFoo.assert_has_calls(fooCalls, any_order=True)
# AssertionError: (call.dooFoo('narf'),) not all found in call list