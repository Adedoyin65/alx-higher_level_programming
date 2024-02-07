#!/usr/bin/python3
"""A module that tests the Base class"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """A class called TestBase that inherit from TestCase"""
    def test_init(self):
        """This is a method to test the init of the Base class"""
        xoo = Base(4)
        yoo = Base()
        self.assertIsInstance(xoo, Base)
        self.assertEqual(xoo.id, 4)
        self.assertEqual(yoo.id, 1)


if __name__ == '__main__':
    unittest.main()
