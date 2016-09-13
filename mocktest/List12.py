# coding: utf-8
from mock import Mock, call


class Foo(object):
    _fooValue = 123

    def callFoo(self):
        pass

    def doFoo(self, argValue):
        pass


# create the mock object
mockFoo = Mock(spec=Foo)
print mockFoo

mockFoo.callFoo()
mockFoo.doFoo("narf")
mockFoo.doFoo("zort")
mockFoo.doFoo("aaaa")
mockFoo.doFoo("bbbb")

fooCalls = [call.callFoo(), call.doFoo("narf"), call.doFoo("zort")]
mockFoo.assert_has_calls(fooCalls)

# 报错, 因为实际调用的顺序与期望的不一致。
# fooCalls = [call.callFoo(), call.doFoo("zort"), call.doFoo("narf")]
# mockFoo.assert_has_calls(fooCalls)

# 不报错, 因为设置了不关心调用顺序。
fooCalls = [call.callFoo(), call.doFoo("zort"), call.doFoo("narf")]
mockFoo.assert_has_calls(fooCalls, any_order=True)

mockFoo.doFoo("bbbb")
mockFoo.doFoo("zort")
mockFoo.doFoo("aaaa")

# 不报错, 因为它的这个顺序不一定要求从起始位置开始,只要执行序列中存在即可
fooCalls = [call.doFoo("aaaa"), call.doFoo("bbbb")]
mockFoo.assert_has_calls(fooCalls)

# 不报错, 因为它的这个顺序不一定要求从起始位置开始,只要执行序列中存在即可
fooCalls = [call.doFoo("bbbb"), call.doFoo("zort")]
mockFoo.assert_has_calls(fooCalls)

# 报错, 因为在填写期望的顺序时不能空。
# fooCalls = [call.doFoo("narf"), call.doFoo("aaaa")]
# mockFoo.assert_has_calls(fooCalls)
