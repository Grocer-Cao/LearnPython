from nose.tools import *
from bin.app import app
from tests.tools import assert_response
import os


def test_Index():
    resp = app.request("/")
    assert_response(resp)


def test_SayHello():
    resp = app.request("/hello")
    assert_response(resp)

    resp = app.request("/hello", method="POST")
    assert_response(resp, contains="Nobody")

    data = {'name':'Oscar','greet':'Hi'}
    resp = app.request("/hello",method="POST",data=data)
    assert_response(resp,contains="Oscar")
