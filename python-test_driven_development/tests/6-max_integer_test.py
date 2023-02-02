#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertAlmostEqual(max_integer([66, 15, 6, 12]), 66)
        self.assertAlmostEqual(max_integer([7, 16, 35, 1, 8]), 35)
        self.assertAlmostEqual(max_integer([9, -9, 18, 14]), 18)
        self.assertAlmostEqual(max_integer([-1, -65, -90, -10]), -1)
        self.assertAlmostEqual(max_integer([9]), 9)
        self.assertAlmostEqual(max_integer([]), None)
