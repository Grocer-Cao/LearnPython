import mock
import unittest

from modular import Count

# class Mock(spec=None,
#            side_effect=None,
#            return_value=DEFAULT,
#            wraps=None,
#            name=None,
#            spec_set=None,
#            **kwargs)

# test Count class
class TestCount(unittest.TestCase):
    def test_add(self):
        count = Count()
        count.add = mock.Mock(return_value=13)
        result = count.add(8, 5)
        self.assertEqual(result, 13)


if __name__ == '__main__':
    unittest.main()
