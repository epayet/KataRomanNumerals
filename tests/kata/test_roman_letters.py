__author__ = 'manu'

import unittest
from roman_letters import to_roman


class RomanLettersTestCase(unittest.TestCase):
    def test_one(self):
        roman = to_roman(1)
        self.assertEqual("I", roman)

    def test_two(self):
        roman = to_roman(2)
        self.assertEqual("II", roman)

    def test_four(self):
        roman = to_roman(4)
        self.assertEqual("IV", roman)

    def test_five(self):
        roman = to_roman(5)
        self.assertEqual("V", roman)


if __name__ == '__main__':
    unittest.main()
