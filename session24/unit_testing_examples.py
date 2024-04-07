"""
TASK
given an integer x, write a program that does the following:

if x is odd, return "red"
if x is even, and in the range of 2 to 5 inclusive, return 'blue
if x is even, and in the range 6 to 20 inclusive, return "red"
if x is even, and greater than 20, return "blue"

constraint input will always be an integer, between 1 and 100

21 red
5 red
20 red
2 blue
99 red
77 red
1 red
24 blue


"""

from unittest import mock, TestCase, main
from .solution import solution_function

class TestRedOrBlueFunction(TestCase):
    def test_odd_numbers(self):
        # 5
        expected_result = 'Red'
        result = solution_function(5)
        self.assertEqual(result, expected_result)

    def test_even_between_2_5(self):
        expected_result = 'Blue'
        actual_result = solution_function(4)
        self.assertEqual(expected_result, actual_result)


    def test_even_between_6_20(self):
        expected_result = 'Red'
        actual_result = solution_function(10)
        self.assertEqual(expected_result, actual_result)

    def test_even_greater_than_20(self):
        expected_result = 'Blue'
        actual_result = solution_function(44)
        self.assertEqual(expected_result, actual_result)
