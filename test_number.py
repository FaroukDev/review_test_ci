import unittest
from reverse_number import Convert


class ReverseTestCase(unittest.TestCase):

    def test_ReverseNumber(self):
        self.assertEqual(Convert([2, 5, 8]), [-2, -5, -8])

if __name__ == '__main__':
    unittest.main()