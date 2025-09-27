"""This module test the age function in age.py"""

import sys
import os
import unittest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from age import categorize_by_age


class TestCategorizeByAge(unittest.TestCase):
    """
    Unit tests for the `categorize_by_age` function.
    """

    def test_child(self) -> None:
        """Tests the Child age range."""
        self.assertEqual(categorize_by_age(5), "Child")

    def test_adolescent(self) -> None:
        """Test the Adolescent age range."""
        self.assertEqual(categorize_by_age(15), "Adolescent")

    def test_adult(self) -> None:
        """Tests the Adult age range."""
        self.assertEqual(categorize_by_age(30), "Adult")

    def test_golden_age(self) -> None:
        """Tests the Golden Age age range."""
        self.assertEqual(categorize_by_age(70), "Golden age")

    def test_negative_age(self) -> None:
        """Tests if a negative age number is given."""
        self.assertEqual(categorize_by_age(-1), "Invalid age: -1")

    def test_too_old(self) -> None:
        """Tests to see if an age given is too old."""
        self.assertEqual(categorize_by_age(151), "Invalid age: 151")

if __name__ == '__main__':
    unittest.main()
# Hello there.