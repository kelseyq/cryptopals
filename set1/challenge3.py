__author__ = 'Kelsey Gilmore-Innis'

from set1 import challenge2

def single_byte_xor(hex_input, byte):
    import itertools
    input_bytes = bytearray.fromhex(hex_input)
    mask = bytearray(itertools.repeat(byte, len(input_bytes)))
    return challenge2.fixed_xor_bytes(input_bytes, mask)

def frequency_score(text):
    lower_text = text.lower()
    space = lower_text.count(' ')
    e = lower_text.count('e')
    t = lower_text.count('t')
    a = lower_text.count('a')
    o = lower_text.count('o')
    i = lower_text.count('i')
    n = lower_text.count('n')
    return space + e + t + a + o + i + n

def detect_single_byte_xor_key(hex_input):
    candidates = [(single_byte_xor(hex_input, byte).decode("latin1"), byte) for byte in range(128)]
    scored_candidates = [(candidate, frequency_score(candidate), byte) for (candidate, byte) in candidates]
    return sorted(scored_candidates, key=lambda candidate: candidate[1], reverse=True)[0]

def decrypt_single_byte_xor(hex_input):
    return detect_single_byte_xor_key(hex_input)[0]
