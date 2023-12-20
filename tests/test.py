import unittest
from triangle import area_triangle
from triangle import perimeter_triangle
from circle import area_circle
from circle import perimeter_circle
from square import area_square
from square import perimeter_square
from rectangle import area_rectangle
from rectangle import perimeter_rectangle


class TriangleTestCase(unittest.TestCase):
    def test_0_mul(self):
        result = area_triangle(7, 8)
        self.assertEqual(result, 28)

    def test_1_mul(self):
        result = area_triangle(10, 5)
        self.assertEqual(result, 25)

    def test_2_mul(self):
        result = area_triangle(7.5, 3.5)
        self.assertEqual(result, 13.125)

    def test_3_mul(self):
        result = perimeter_triangle(0, 0, 0)
        self.assertEqual(result, 0)


    def test_4_mul(self):
        result = perimeter_triangle(10, 4, 8)
        self.assertEqual(result, 22)


    def test_five_mul(self):
        result = perimeter_triangle(34.23, 42.34, 23.43)
        self.assertEqual(result, 100)



class SquareTestCase(unittest.TestCase):

    def test_zero_mul(self):
        result = area_square(0)
        self.assertEqual(result, 0)

    def test_one_mul(self):
        result = area_square(10)
        self.assertEqual(result, 100)


    def test_two_mul(self):
        result = area_square(7.5)
        self.assertEqual(result, 56.25)

    def test_three_mul(self):
        result = perimeter_circle(0)
        self.assertEqual(result, 0)


    def test_four_mul(self):
        result = perimeter_circle(10)
        self.assertEqual(result, 62.83185307179586)

    def test_five_mul(self):
        result = perimeter_circle(17.25)
        self.assertEqual(result, 108.38494654884786)



class RectangleTestCase(unittest.TestCase):

    def test_zero_mul(self):
        result = area_rectangle(0,13)
        self.assertEqual(result, 0)

    def test_one_mul(self):
        result = area_rectangle(10,13)
        self.assertEqual(result, 130)

    def test_two_mul(self):
        result = area_rectangle(67.5,3.5)
        self.assertEqual(result, 236.25)

    def test_three_mul(self):
        result = perimeter_rectangle(0,0)
        self.assertEqual(result, 0)

    def test_four_mul(self):
        result = perimeter_rectangle(10,54)
        self.assertEqual(result, 128)

    def test_five_mul(self):
        result = perimeter_rectangle(67.636,42.364)
        self.assertEqual(result,220)

class CircleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        result = area_circle(0)
        self.assertEqual(result, 0)

    def test_one_mul(self):
        result = area_circle(10)
        self.assertEqual(result, 314.1592653589793)

    def test_two_mul(self):
        result = area_circle(67.636)
        self.assertEqual(result, 14371.619275936122)

    def test_three_mul(self):
        result = perimeter_circle(0)
        self.assertEqual(result, 0)


    def test_four_mul(self):
        result = perimeter_circle(10)
        self.assertEqual(result, 62.83185307179586)

    def test_five_mul(self):
        result = perimeter_circle(67.636)
        self.assertEqual(result, 424.96952143639845)

if __name__ == '__main__':
    unittest.main()

