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

    def test_height(self):
        boo = Rectangle(3, 5)
        self.assertEqual(boo.height, 5)
        boo.height = 10
        self.assertEqual(boo.height, 10)

    def test_x(self):
        too = Rectangle(1, 1, 2)
        self.assertEqual(too.x, 2)
        too.x = 1
        self.assertEqual(too.x, 1)

    def test_y(self):
        zoo = Rectangle(1, 1, 2, 6)
        self.assertEqual(zoo.y, 6)
        zoo.y = 7
        self.assertEqual(zoo.y, 7)

    def test_area(self):
        roo = Rectangle(3, 4, 5, 6)
        self.assertEqual(roo.area(), 12)


if __name__ == '__main__':
    unittest.main()
