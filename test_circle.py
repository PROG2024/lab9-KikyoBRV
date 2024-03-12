"""Unit tests of the Circle class using unittest or pytest (your choice).

Write unit tests as described in README.md.

1. Unit test for add_area using typical values.
2. Unit test for add_area for an "edge case" where one circle has radius 0.
3. Unit test that circle constructor raises exception of radius is negative.

"""
import math
import unittest
from circle import Circle


class TestCircle(unittest.TestCase):

    def test_add_area_typical_case(self):
        # Typical case: Test add_area with two circles having positive radii.
        circle1 = Circle(3)
        circle2 = Circle(4)
        result_circle = circle1.add_area(circle2)

        self.assertAlmostEqual(result_circle.get_radius(), 5, places=6)
        self.assertAlmostEqual(result_circle.get_area(),
                               math.pi*(result_circle.get_radius()**2), places=100)

    def test_add_area_edge_case_zero_radius(self):
        # Edge case: Test add_area when one of the circles has radius 0,
        # the other has non-zero radius. (Result should have same radius.)
        circle1 = Circle(0)
        circle2 = Circle(5)
        result_circle1 = circle1.add_area(circle2)
        result_circle2 = circle2.add_area(circle1)

        self.assertAlmostEqual(result_circle1.get_radius(), 5, places=6)
        self.assertAlmostEqual(result_circle2.get_radius(), 5, places=6)
        self.assertAlmostEqual(result_circle1.get_area(),
                               math.pi*(result_circle1.get_radius()**2), places=6)
        self.assertAlmostEqual(result_circle2.get_area(),
                               math.pi*(result_circle2.get_radius()**2), places=6)

    def test_constructor_negative_radius(self):
        # Test that Circle constructor raises exception if the radius is negative.
        with self.assertRaises(ValueError):
            circle = Circle(-2)


if __name__ == '__main__':
    unittest.main()

