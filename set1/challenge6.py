__author__ = 'Kelsey Gilmore-Innis'

from set1 import challenge2, challenge3, challenge5


def hamming_distance(first_bytes, second_bytes):
    import bitstring
    xor = challenge2.fixed_xor_bytes(first_bytes, second_bytes)
    return bitstring.Bits(xor).count(1)


def key_likelihood(input_bytes, key_size):
    import itertools
    import math
    total_distances = 0
    max_blocks_to_compare = 10
    max_repeats = math.floor(len(input_bytes) / key_size)
    blocks_to_compare = min(max_blocks_to_compare, max_repeats)
    combos = list(itertools.combinations(range(0, blocks_to_compare), 2))
    for (first, second) in combos:
        block1 = input_bytes[(first * key_size):((first + 1) * key_size)]
        block2 = input_bytes[(second * key_size):((second + 1) * key_size)]
        total_distances += hamming_distance(block1, block2)
    avg_distance = total_distances / len(combos)
    return avg_distance / key_size


def find_key_size(input_bytes, min_key_size=2, max_key_size=40):
    key_size_scores = [(key_size, key_likelihood(input_bytes, key_size))
                       for key_size in range(min_key_size, max_key_size)]
    best = sorted(key_size_scores, key=lambda score: score[1])
    return best[0][0]


def break_repeating_xor_bytes(input_bytes):
    key_size = find_key_size(input_bytes)
    chunks = [input_bytes[i:i + key_size] for i in range(0, len(input_bytes), key_size)]
    transposed_chunks = [[chunk[i] for chunk in chunks[:-1]] for i in range(0, key_size)]
    key_bytes = [challenge3.detect_single_byte_xor_key(transposed_chunk)[2] for transposed_chunk in transposed_chunks]
    key = bytearray(key_bytes).decode("ascii")
    return challenge5.encrypt_repeating_key(input_bytes, key)


def break_repeating_xor():
    import os
    import base64
    fn = os.path.join(os.path.dirname(__file__), 'resources', 'challenge6.txt')
    with open(fn) as f:
        return break_repeating_xor_bytes(base64.b64decode(f.read()))
