import unittest
from reverse import my_function

class TestStringMethods(unittest.TestCase):
    def test_ReverseTestCase(self):
        self.assertEqual(my_function('hello les noobs'), 'sboon sel olleh')

if __name__ == '__main__':
    unittest.main()

