#!/usr/bin/python3
"""A module that tests the Base class"""
import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """A class called TestBase that inherit from TestCase"""
    def test_uuid(self):
        x = Base()
        y = Base()
        self.assertIsInstance(x, Base)
        self.assertNotEqual(x.id, y.id)
if __name__ == '__main__':
    unittest.main()
