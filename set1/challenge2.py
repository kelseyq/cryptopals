__author__ = 'Kelsey Gilmore-Innis'


def fixed_xor_bytes(input_one_bytes, input_two_bytes):
    if len(input_one_bytes) != len(input_two_bytes):
        raise ValueError("byte strings must be the same length")
    xor = [a ^ b for a, b in zip(input_one_bytes, input_two_bytes)]
    return bytes(xor)


def fixed_xor_hex(input_one_hex, input_two_hex):
    input_one_bytes = bytearray.fromhex(input_one_hex)
    input_two_bytes = bytearray.fromhex(input_two_hex)
    return fixed_xor_bytes(input_one_bytes, input_two_bytes)
