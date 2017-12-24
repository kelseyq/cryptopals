from set1 import challenge3


def detect_single_byte_xor():
    import os
    fn = os.path.join(os.path.dirname(__file__), 'resources', 'challenge4.txt')
    with open(fn) as f:
        likelies = [challenge3.detect_single_byte_xor_key(bytearray.fromhex(line.strip())) for line in f]
        best = sorted(likelies, key=lambda likely: likely[1], reverse=True)[0]
        return best[0]
