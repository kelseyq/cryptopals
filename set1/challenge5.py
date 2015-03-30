__author__ = 'Kelsey Gilmore-Innis'

from set1 import challenge2

def encrypt_repeating_key(bytes, key):
    import math
    repeats = math.ceil(len(bytes) / len(key))
    mask = bytearray((key * repeats)[:len(bytes)], "latin1")
    encrypted = challenge2.fixed_xor_bytes(bytes, mask)
    return encrypted
