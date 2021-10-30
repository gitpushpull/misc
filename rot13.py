import unittest


def rot13(str_in):
    str_out = ""
    for char_in in str_in:
        if 'A' <= char_in <= 'Z':
            str_out += chr(ord('A') + (ord(char_in) - ord('A') + 13) % 26) 
        elif 'a' <= char_in <= 'z':
            str_out += chr(ord('a') + (ord(char_in) - ord('a') + 13) % 26)
        else:
            str_out += char_in

    return str_out


class Tests(unittest.TestCase):
    def test_alpha(self):
        test_strs = ['this is a test string', 'asfsjfhjfsd fasdsaf oruewoufh', 'a', 'asf243rf4']
        for test_str in test_strs:
            str_cipher = rot13(test_str)
            self.assertNotEqual(str_cipher, test_str)
            str_plain = rot13(str_cipher)
            self.assertEqual(str_plain, test_str)

    def test_num(self):
        test_str = '123457567'
        str_cipher = rot13(test_str)
        self.assertEqual(str_cipher, test_str)
        str_plain = rot13(str_cipher)
        self.assertEqual(str_plain, test_str)

if __name__ == '__main__':
    unittest.main()