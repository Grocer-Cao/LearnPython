# coding: utf-8
from mock import patch
from bin.app import app
import unittest
import web
from tests.tools import assert_response

render = web.template.render('templates/', base="layout")


class MyTestCase(unittest.TestCase):
    @patch("bin.app.index.GET")
    def test_indexGET(self, mock_indexGET):
        mock_indexGET.return_value = render.index(greeting="112358")
        resp = app.request("/")

        mock_indexGET.assert_called_once_with()
        assert_response(resp, contains="112358")

    @patch("bin.app.caoPH.GET")
    def test_caoPHGET(self, mock_caoPHGET):
        mock_caoPHGET.return_value = "aabbcc"
        resp = app.request("/cph")

        mock_caoPHGET.assert_called_once_with()
        assert_response(resp, status="200")

    @patch("bin.app.hello.GET")
    def test_helloGET(self,mock_helloGET):
        mock_helloGET.return_value = render.hello(greeting="hello——GET", another="Another line")
        resp = app.request("/hello")

        mock_helloGET.assert_called_once_with()
        assert_response(resp, status="200")
        assert_response(resp, contains="Another line")

    @patch("bin.app.fillform.GET")
    def test_helloGET(self, mock_fillformGET):
        mock_fillformGET.return_value = render.fform()
        resp = app.request("/fillform")

        mock_fillformGET.assert_called_once_with()
        assert_response(resp, status="200")

    @patch("bin.app.fillform.POST")
    def test_helloGET(self, mock_fillformPOST):
        mock_fillformPOST.return_value = render.hello(greeting="Hi, Grocer", another="Another line")
        # app的request方法有参数method可以设置为POST,这样将会访问到fillform的POST方法
        # 由于前面已经mock了fillform的返回值,所以这里不用指定输入的data,即使指定了也没有用,它将会按mock中规定的值返回。
        resp = app.request(localpart="/fillform",method='POST')

        mock_fillformPOST.assert_called_once_with()
        assert_response(resp, status="200")
        assert_response(resp, contains="Hi, Grocer")

if __name__ == '__main__':
    unittest.main()
