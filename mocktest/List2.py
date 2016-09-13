# coding: utf-8
from mock import Mock

# property属性_fooValue,方法属性callFoo和doFoo
fooSpec = ["_fooValue", "callFoo", "doFoo"]

mockFoo = Mock(spec=fooSpec)

print mockFoo

print mockFoo._fooValue

print mockFoo.callFoo()

mockFoo.callFoo()

# 访问未声明属性时将会报错
# print mockFoo._fooBar
# mockFoo.callFoobar()
