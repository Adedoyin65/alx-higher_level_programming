#!/usr/bin/python3
"""A module that tests the file rectangle and the methods"""
import unittest
from models.rectangle import Rectangle


class TestRec(unittest.TestCase):
    """A class(TestRec) that inherits from TestCase"""
    def test_init(self):
        """This method is to test the init method of Rectangle class"""
        guv = Rectangle(2, 3, 4, 5)
        self.assertEqual(guv.width, 2)
        self.assertEqual(guv.height, 3)
        self.assertEqual(guv.x, 4)
        self.assertEqual(guv.y, 5)

    def test_width(self):
        """This method is to test the width atrribute of the Rectangle"""
        doo = Rectangle(7, 9)
        self.assertEqual(doo.width, 7)
        doo.width = 9
        self.assertEqual(doo.width, 9)

    def test_height(self):
        """This method is to test the height attribute of the rectangle"""
        boo = Rectangle(3, 5)
        self.assertEqual(boo.height, 5)
        boo.height = 10
        self.assertEqual(boo.height, 10)

    def test_x(self):
        """This method is to test the x attribute of the rectangle"""
        too = Rectangle(1, 1, 2)
        self.assertEqual(too.x, 2)
        too.x = 1
        self.assertEqual(too.x, 1)

    def test_y(self):
        """This method is to test the y attribute of the rectangle"""
        zoo = Rectangle(1, 1, 2, 6)
        self.assertEqual(zoo.y, 6)
        zoo.y = 7
        self.assertEqual(zoo.y, 7)

    def test_area(self):
        """This method is to test the area method of the Rectangle"""
        roo = Rectangle(3, 4, 5, 6)
        self.assertEqual(roo.area(), 12)


if __name__ == '__main__':
    unittest.main()
