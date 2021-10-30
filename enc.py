import base64


def enc(plain_text):
    return base64.b16encode(plain_text.encode("utf-8"))


def dec(enc_text):
    return base64.b16decode(enc_text).decode("utf-8")


