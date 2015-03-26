__author__ = 'Kelsey Gilmore-Innis'

def fixed_xor(input_one, input_two):
    input_one_bytes = bytearray.fromhex(input_one)
    input_two_bytes = bytearray.fromhex(input_two)
    if len(input_one_bytes) != len(input_two_bytes):
        raise ValueError("save must be True if recurse is True")
    return bytearray([a ^ b for a, b in zip(input_one_bytes, input_two_bytes)])