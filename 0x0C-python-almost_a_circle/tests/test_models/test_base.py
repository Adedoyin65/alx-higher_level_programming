#!/usr/bin/python3
"""A module that tests the Base class"""
import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """A class called TestBase that inherit from TestCase"""
    def test_init(self):
        x = Base(4)
        y = Base()
        self.assertIsInstance(x, Base)
        self.assertEqual(x.id, 4)
        self.assertEqual(y.id, 1)
if __name__ == '__main__':
    unittest.main()
