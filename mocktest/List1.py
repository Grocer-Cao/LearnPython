from mock import Mock

# create the mock object
mockFoo = Mock(name="Foo")

print mockFoo
# returns: <Mock name='Foo' id='4329714768'>
print repr(mockFoo)
# still returns: <Mock name='Foo' id='4329714768'>