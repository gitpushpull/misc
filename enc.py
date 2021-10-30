import base64


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

