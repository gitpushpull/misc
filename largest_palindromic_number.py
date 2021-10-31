"""Largest palindromic number less than max_numb which is the product of two 3-digit numbers."""
""" 913 * 993 = 906609 """
import math
import unittest

def is_palindrome(num_str):
    return num_str == num_str[::-1]

def largest_palindrome(max_numb):
    lp = 0

    for i in range(999, 99, -1):  # 3 digit numbers range from 999 down to 100
        for j in range(999, 99, -1):
            prod = i * j
            if prod < max_numb and is_palindrome(str(prod)):
                lp = max(lp, prod)
    return lp


class Tests(unittest.TestCase):
    def test_largest_palindrome(self):
        prod = largest_palindrome(999 * 999)  # = 998001
        self.assertEqual(prod, 906609)
        
        prod = largest_palindrome(900 * 800)  # = 720000
        self.assertEqual(prod, 698896)

        prod = largest_palindrome(600 * 600)  # = 360000
        self.assertEqual(prod, 359953)

        prod = largest_palindrome(100 * 200)  # = 20000
        self.assertEqual(prod, 19591)

if __name__ == '__main__':
    unittest.main()