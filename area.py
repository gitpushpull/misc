from math import pi, sqrt
import unittest


class Area:
    def square(self, side):
        return side ** 2

    def rect(self, width, height):
        return width * height

    def circle(self, radius):
        return pi * radius ** 2

    def triangle(self, base, height):
        return (base * height) / 2

areas = Area()

def truncate(fl_num, n):
    str_num = str(fl_num)
    period_idx = str_num.find('.')
    if len(str_num) < period_idx + n + 1:
        str_num += '0' * (period_idx + n + 1 - len(str_num))        
    return float(str_num[0:period_idx + n + 1])

class Tests(unittest.TestCase):
    def test_square(self):
        self.assertEqual(areas.square(4), 16)

    def test_rect(self):
        self.assertEqual(areas.rect(3, 4), 12)

    def test_circle(self):
        self.assertAlmostEqual(truncate(areas.circle(4), 2), 50.26, 2)

    def test_triangle(self):
        self.assertAlmostEqual(truncate(areas.triangle(3, 4), 2), 6.00, 2)

if __name__ == '__main__':
    unittest.main()
