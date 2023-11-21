import math
import unittest

def area_circle(r):
    '''Принимает число r-радиус окружности, возвращает её площадь'''
    return math.pi * r * r


def perimeter_circle(r):
    '''Принимает число r-радиус окружности, возвращает её длину'''
    return 2 * math.pi * r


class CircleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area_circle(0)
        self.assertEqual(res, 0)

    def test_one_mul(self):
        res = area_circle(10)
        self.assertEqual(res, 314.1592653589793)

    def test_two_mul(self):
        res = area_circle(67.636)
        self.assertEqual(res, 14371.619275936122)

    def test_three_mul(self):
        res = perimeter_circle(0)
        self.assertEqual(res, 0)

    def test_four_mul(self):
        res = perimeter_circle(10)
        self.assertEqual(res, 62.83185307179586)

    def test_five_mul(self):
        res = perimeter_circle(67.636)
        self.assertEqual(res, 424.96952143639845)