def detect_aes_in_ecb_challenge():
    import os
    fn = os.path.join(os.path.dirname(__file__), 'resources', 'challenge8.txt')
    with open(fn) as f:
        lines = f.readlines()
        return lines[0]
