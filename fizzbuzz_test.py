import unittest
from unittest.mock import patch, call
from fizzbuzz import fizzbuzz

class TestFizzBuzz(unittest.TestCase):
    @patch('builtins.print')
    def test_fizz(self, mocked_print):
        fizzbuzz(3)
        self.assertEqual(mocked_print.mock_calls, [call('Fizz')])

    @patch('builtins.print')
    def test_buzz(self, mocked_print):
        fizzbuzz(5)
        self.assertEqual(mocked_print.mock_calls, [call('Buzz')])

    @patch('builtins.print')
    def test_fizzbuzz(self, mocked_print):
        fizzbuzz(15)
        self.assertEqual(mocked_print.mock_calls, [call('FizzBuzz')])

    @patch('builtins.print')
    def test_non_fizzbuzz(self, mocked_print):
        fizzbuzz(4)
        self.assertEqual(mocked_print.mock_calls, [call(4)])
