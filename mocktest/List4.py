# coding: utf-8
from mock import Mock

mockFoo = Mock(return_value=456)

mockObj = mockFoo()
print mockObj
