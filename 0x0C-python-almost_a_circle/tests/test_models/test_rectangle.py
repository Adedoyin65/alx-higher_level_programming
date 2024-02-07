#!/usr/bin/python3
"""A module that tests the file rectangle and the methods"""
import unittest
from models.rectangle import Rectangle



class TestRec(unittest.TestCase):
    """A class(TestRec) that inherits from TestCase"""
    def test_init(self):
        guv = Rectangle(2, 3, 4, 5)
        self.assertEqual(guv.width, 2)
        self.assertEqual(guv.height, 3)
        self.assertEqual(guv.x, 4)
        self.assertEqual(guv.y, 5)

    def test_width(self):
        foo = Rectangle(7, 9)
        self.assertEqual(foo.width, 7)
        foo.width = 9
        self.assertEqual(foo.width, 9)
if __name__ == '__main__':
    unittest.main()
