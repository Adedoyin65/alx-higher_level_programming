#!/usr/bin/python3
"""A module that tests the Base class"""
import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """A class called TestBase that inherit from TestCase"""
    def test_init(self):
        x = Base(4)
        y = Base(4)
        self.assertIsInstance(x, Base)
        self.assertEqual(x.id, y.id)
if __name__ == '__main__':
    unittest.main()
