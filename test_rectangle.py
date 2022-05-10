from unittest import TestCase
from rectangle import Rectangle


class TestRectangle(TestCase):

    def setUp(self):
        self.rectangle = Rectangle(30, 15)

    def test_area(self):

        area = self.rectangle.area()
        print(area)
        self.assertEqual(area, 450)

    def test_perimeter(self):

        perimeter = self.rectangle.perimeter()
        self.assertEqual(perimeter, 90)

    def test_diff(self):

        diff = self.rectangle.diff()
        self.assertEqual(diff, 15)

    def test_resize(self):

        self.assertRaises(ValueError, self.rectangle.resize, 15, 0)

    def tearDown(self):
        self.rectangle = None
