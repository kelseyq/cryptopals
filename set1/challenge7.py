def decrypt_aes_in_cbc_challenge():
    import os
    import base64
    fn = os.path.join(os.path.dirname(__file__), 'resources', 'challenge7.txt')
    with open(fn) as f:
        return base64.b64decode(f.read())
