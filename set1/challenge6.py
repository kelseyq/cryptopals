__author__ = 'Kelsey Gilmore-Innis'

from set1 import challenge2

def hamming_distance(first_bytes, second_bytes):
    import bitstring
    xor = challenge2.fixed_xor_bytes(first_bytes, second_bytes)
    return bitstring.Bits(xor).count(1)

def key_likelihood(bytes, key_size):
    import itertools, math
    total_distances = 0
    max_blocks_to_compare = 10
    max_repeats = math.floor(len(bytes) / key_size)
    blocks_to_compare = min(max_blocks_to_compare, max_repeats)
    combos = list(itertools.combinations(range(0, blocks_to_compare), 2))
    for (first, second) in combos:
        block1 = bytes[(first * key_size):((first + 1) * key_size)]
        block2 = bytes[(second * key_size):((second + 1) * key_size)]
        total_distances += hamming_distance(block1, block2)
    avg_distance = total_distances / len(combos)
    return avg_distance / key_size

def find_key_size(bytes, min_key_size = 2, max_key_size=40):
    key_size_scores = [(key_size, key_likelihood(bytes, key_size)) for key_size in range(min_key_size, max_key_size)]
    best = sorted(key_size_scores, key=lambda score: score[1])
    return best[0][0]

def break_repeating_xor():
    import os, base64
    fn = os.path.join(os.path.dirname(__file__), 'resources', 'challenge4.txt')
    with open(fn) as f:
        file_bytes = base64.b64decode(f.read)
        find_key_size(file_bytes)