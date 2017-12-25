from Crypto.Cipher import AES


def decrypt_aes_in_ecb_mode(text_string, key_bytes):
    import base64
    cipher = AES.new(key_bytes, AES.MODE_ECB)
    decrypted = cipher.decrypt(base64.b64decode(text_string))
    return decrypted


def decrypt_aes_in_ecb_challenge():
    import os
    fn = os.path.join(os.path.dirname(__file__), 'resources', 'challenge7.txt')
    with open(fn) as f:
        key = b'YELLOW SUBMARINE'
        return decrypt_aes_in_ecb_mode(f.read(), key)
