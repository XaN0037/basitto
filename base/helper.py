import binascii
import os

from rest_framework.authentication import TokenAuthentication
import base64


def code_decoder(code, decode=False):
    if decode:
        return base64.b64decode(code).decode()
    else:
        return base64.b64encode(f"{code}".encode("utf-8")).decode()


def generate_key(cls):
    return binascii.hexlify(os.urandom(cls)).decode()

# text = input('suz kiriting: ')
#
# new_text = text[0].upper() + text[1:]
# print(new_text)
