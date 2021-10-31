import unittest

enc_codes = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.",
    "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..", "M": "--", "N": "-.",
    "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-", "U": "..-",
    "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--", "Z": "--..",
    "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....", "6": "-....",
    "7": "--...", "8": "---..", "9": "----.", "0": "-----", "&": ".-...", "@": ".--.-.",
    ":": "---...", ",": "--..--", ".": ".-.-.-", "'": ".----.", '"': ".-..-.",
    "?": "..--..", "/": "-..-.", "=": "-...-", "+": ".-.-.", "-": "-....-",
    "(": "-.--.", ")": "-.--.-", "!": "-.-.--", " ": "/"
}

dec_codes =  {v: k for k, v in enc_codes.items()}  # {".-" : "A", "-...": "B"} etc.

def morse_enc(msg):
    return " ".join(enc_codes[ch] for ch in msg.upper())

def morse_dec(msg):
    return "".join(dec_codes[ch] for ch in msg.split())    


class Tests(unittest.TestCase):
    def test_enc(self):
        self.assertEqual(morse_enc('sms'), '... -- ...')
        self.assertEqual(morse_enc('sos'), '... --- ...')

    def test_dec(self):
        self.assertEqual('... -- ...', morse_enc('sms'))
        self.assertEqual('... --- ...', morse_enc('sos'))

if __name__ == '__main__':
    unittest.main()
