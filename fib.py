import unittest

def get_fib(max_count):
    i = 1
    j = 2
    fib_seq = []
    while len(fib_seq) < max_count:
        fib_seq.append(j)
        i, j = j, i + j

    return fib_seq


class Tests(unittest.TestCase):
    def test_fib(self):
        fib_seq_check = [2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
        fib_seq = get_fib(len(fib_seq_check))
        
        self.assertEqual(fib_seq, fib_seq_check)
    
if __name__ == '__main__':
    unittest.main()
