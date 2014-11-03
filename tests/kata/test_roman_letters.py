__author__ = 'manu'

import unittest
from roman_letters import *


class ToRomanTestCase(unittest.TestCase):
    def test_one(self):
        roman = to_roman(1)
        self.assertEqual("I", roman)

    def test_eleven(self):
        roman = to_roman(11)
        self.assertEqual("XI", roman)

    def test_complex_number(self):
        roman = to_roman(1990)
        self.assertEqual("MCMXC", roman)

    def test_complex_number2(self):
        roman = to_roman(2008)
        self.assertEqual("MMVIII", roman)


class GetIsolatedRomanLetter(unittest.TestCase):
    def test_get_one(self):
        roman = get_isolated_roman(1)
        self.assertEqual("I", roman)

    def test_get_two(self):
        roman = get_isolated_roman(2)
        self.assertEqual("II", roman)

    def test_get_four(self):
        roman = get_isolated_roman(4)
        self.assertEqual("IV", roman)

    def test_get_five(self):
        roman = get_isolated_roman(5)
        self.assertEqual("V", roman)

    def test_get_seven(self):
        roman = get_isolated_roman(7)
        self.assertEqual("VII", roman)

    def test_get_twenty(self):
        roman = get_isolated_roman(20)
        self.assertEqual("XX", roman)

    def test_get_thousand(self):
        roman = get_isolated_roman(1000)
        self.assertEqual("M", roman)

    def test_get_nine_hundred(self):
        roman = get_isolated_roman(900)
        self.assertEqual("CM", roman)

    def test_get_4000(self):
        roman = get_isolated_roman(4000)
        self.assertEqual("MMMM", roman)


class GetIsolatedNumbersTestCas(unittest.TestCase):
    def test_get_one(self):
        isolated = get_isolated_numbers(1)
        self.assertEqual([1], isolated)

    def test_get_eleven(self):
        isolated = get_isolated_numbers(11)
        self.assertEqual([10, 1], isolated)

    def test_get_big_number(self):
        isolated = get_isolated_numbers(1990)
        self.assertEqual([1000, 900, 90], isolated)

    def test_get_big_number_2(self):
        isolated = get_isolated_numbers(2008)
        self.assertEqual([2000, 8], isolated)


class GetNumberPositionInStepTestCase(unittest.TestCase):
    def test_get_first_step(self):
        position = get_number_position_in_step(4)
        self.assertEqual(4, position)

    def test_get_second_step(self):
        position = get_number_position_in_step(5)
        self.assertEqual(0, position)

    def test_get_third_step(self):
        position = get_number_position_in_step(40)
        self.assertEqual(4, position)

    def test_get_fourth_step(self):
        position = get_number_position_in_step(70)
        self.assertEqual(2, position)

    def test_get_fifth_step(self):
        position = get_number_position_in_step(400)
        self.assertEqual(4, position)

    def test_get_sixth_step(self):
        position = get_number_position_in_step(600)
        self.assertEqual(1, position)

    def test_get_seventh_step(self):
        position = get_number_position_in_step(3000)
        self.assertEqual(3, position)


class GetCurrentStepTestCase(unittest.TestCase):
    def test_0(self):
        step = get_current_step(1)
        self.assertEqual(0, step)

    def test_1(self):
        step = get_current_step(7)
        self.assertEqual(1, step)

    def test_get_last(self):
        step = get_current_step(2000)
        self.assertEqual(6, step)


class IsStartWith5TestCase(unittest.TestCase):
    def test_is(self):
        self.assertEqual(True, is_start_with_5(50))

    def test_is_not(self):
        self.assertEqual(False, is_start_with_5(1))


if __name__ == '__main__':
    unittest.main()
