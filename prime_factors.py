import math
import unittest

def is_prime(numb):
    if numb % 2 == 0 and numb > 2:
        return False

    numb_sqrt = int(math.sqrt(numb))

    return all(numb % i for i in range(3, numb_sqrt + 1, 2))

def prime_factors(numb):
    factors = []
    if is_prime(numb):
        factors.append(numb)
    else:
        for i in range(2, numb + 1):
            if is_prime(i) and numb % i == 0:
                factors.append(i)
    return factors

class Tests(unittest.TestCase):
    def test_prime_factors(self):
        pfs_check = {15:[3,5], 70:[2,5,7], 91:[7, 13], 283:[283], 363:[3, 11], 1000:[2, 5]}
        for p in pfs_check:
            pfs = prime_factors(p)
            self.assertEqual(pfs, pfs_check[p])

if __name__ == '__main__':
    unittest.main()