import mock
import unittest
import webclient


class TestClient(unittest.TestCase):
    def test_success_request(self):
        success_send = mock.Mock(return_value='200')
        webclient.send_request = success_send
        self.assertEqual(webclient.visit_utack(), '200')

    def test_fail_request(self):
        fail_send = mock.Mock(return_value='404')
        webclient.send_request = fail_send
        self.assertEqual(webclient.visit_utack(), '404')


if __name__ == '__main__':
    unittest.main()
