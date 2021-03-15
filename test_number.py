import unittest
from reverse_number import Convert


class TestStringMethods(unittest.TestCase):

    def ReverseNumber(self):
        self.assertEqual(Convert('[2, 5, 8]'), '[-2, -5, -8]')

if __name__ == '__main__':
    unittest.main()