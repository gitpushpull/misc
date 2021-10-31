import base64
import unittest


def enc16(plain_text):
    return base64.b16encode(plain_text.encode("utf-8"))


def dec16(enc_text):
    return base64.b16decode(enc_text).decode("utf-8")


def enc32(plain_text):
    return base64.b32encode(plain_text.encode("utf-8"))


def dec32(enc_text):
    return base64.b32decode(enc_text).decode("utf-8")

def enc64(plain_text):
    return base64.b64encode(plain_text.encode("utf-8"))


def dec64(enc_text):
    return base64.b64decode(enc_text).decode("utf-8")

msgs = {
	'hello world': [b'68656C6C6F20776F726C64', b'NBSWY3DPEB3W64TMMQ======', b'aGVsbG8gd29ybGQ='],
	'HELLO WORLD': [b'48454C4C4F20574F524C44', b'JBCUYTCPEBLU6USMIQ======', b'SEVMTE8gV09STEQ=']
}


class Tests(unittest.TestCase):
    def test_enc(self):
        for msg in msgs:
            self.assertEqual(msgs[msg][0], enc16(msg))
            self.assertEqual(msgs[msg][1], enc32(msg))
            self.assertEqual(msgs[msg][2], enc64(msg))

    def test_dec(self):
        for msg in msgs:
            self.assertEqual(msg, dec16(msgs[msg][0]))
            self.assertEqual(msg, dec32(msgs[msg][1]))
            self.assertEqual(msg, dec64(msgs[msg][2]))

if __name__ == '__main__':
    unittest.main()
