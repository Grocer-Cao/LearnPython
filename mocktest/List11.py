# coding: utf-8
from mock import Mock

class Foo(object):
    _fooValue = 123

    def callFoo(self):
        pass

    def doFoo(self, argValue):
        pass

mockFoo = Mock(spec=Foo)
print mockFoo

mockFoo.callFoo()
mockFoo.doFoo("narf")
mockFoo.doFoo("zort")

mockFoo.callFoo.assert_any_call()

mockFoo.callFoo()
mockFoo.doFoo("troz")

# 不报错,因为assert_any_call会检测之前的所有调用,
# 只要有符合要求的调用就不会报错
mockFoo.doFoo.assert_any_call("zort")

# 报错,由于它找不到之前有调用时传递过"egad"参数
# mockFoo.doFoo.assert_any_call("egad")
