__author__ = 'Kelsey Gilmore-Innis'

from set1 import challenge2

def encrypt_repeating_key(text, key):
    import math, binascii
    repeats = math.ceil(len(text) / len(key))
    mask = bytearray((key * repeats)[:len(text)], "utf-8")
    encrypted = challenge2.fixed_xor_bytes(text.encode("utf-8"), mask)
    return binascii.hexlify(encrypted)