__author__ = 'Kelsey Gilmore-Innis'

from set1 import challenge2

def encrypt_repeating_key(input_bytes, key):
    import math
    repeats = math.ceil(len(input_bytes) / len(key))
    mask = bytearray((key * repeats)[:len(input_bytes)], "ascii")
    encrypted = challenge2.fixed_xor_bytes(input_bytes, mask)
    return encrypted
