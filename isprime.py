import math
import unittest

def is_prime(numb):
    if numb % 2 == 0 and numb > 2:
        return False

    numb_sqrt = int(math.sqrt(numb))

    return all(numb % i for i in range(3, numb_sqrt + 1, 2))


class Tests(unittest.TestCase):
    def test_prime(self):
        primes = [2, 3, 599, 827, 1093, 7919]
        for p in primes:
            self.assertTrue(is_prime(p))

    def test_not_prime(self):
        primes = [4, 9, 15, 27, 339, 1001]
        for p in primes:
            self.assertFalse(is_prime(p))

if __name__ == '__main__':
    unittest.main()