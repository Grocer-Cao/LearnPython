# coding: utf-8
from mock import patch
from bin.app import app
import unittest
import web
from tests.tools import assert_response

render = web.template.render('templates/', base="layout")


class MyTestCase(unittest.TestCase):
    @patch("bin.app.index.GET")
    def test_index(self, mock_GET):
        mock_GET.return_value = render.index(greeting="112358")

        resp = app.request("/")

        mock_GET.assert_called_once_with()

        assert_response(resp, contains="112358")


if __name__ == '__main__':
    unittest.main()
