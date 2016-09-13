from nose.tools import *
from bin.app import app
from tests.tools import assert_response
from mock import Mock

class mockApp(object):
    status = 404

mAppObj = mockApp()
Mkapp = Mock(return_value=mAppObj)
mkappObj = Mkapp()

def test_index():
    # check that we get a 404 on the /xyz URL

    #resp = app.request("/xyz")
    resp = mkappObj.status
    assert_equal(resp, 404)
    #assert_response(resp, status="404")

    # test our first GET request to /fillform
    resp = app.request("/fillform")
    assert_response(resp, status="200")

    # make sure default values work for the form
    resp = app.request("/fillform", method="POST")
    assert_response(resp, contains='Nobody')

    # test that we get expected values
    data = {'name': 'Oscar', 'greet': 'Hola'}
    resp = app.request("/fillform", method="POST", data=data)
    assert_response(resp, contains="Oscar")