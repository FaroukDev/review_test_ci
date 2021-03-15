import unittest
from reverse import my_function
from reverse_number import Convert


class TestStringMethods(unittest.TestCase):
    def ReverseTestCase(self):
        self.assertEqual(my_function('hello les noobs'), 'sboon sel olleh')

    def ReverseNumber(self):
        self.assertEqual(Convert('[2, 5, 8]'), '[-2, -5, -8]')

if __name__ == '__main__':
    unittest.main()

