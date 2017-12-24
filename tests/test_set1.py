import unittest
from set1 import challenge1, challenge2, challenge3, challenge4, challenge5, challenge6, challenge7


class Set1TestCase(unittest.TestCase):
    def with_file(self, filename, function):
        import os
        fn = os.path.join(os.path.dirname(__file__), 'resources', filename)
        with open(fn) as f:
            return function(f)


class Challenge1(Set1TestCase):
    def test_convert_to_base64_nonhex(self):
        self.assertRaises(ValueError, challenge1.convert_to_base64, "this is not a hex string")

    def test_convert_to_base64(self):
        self.assertEqual(challenge1.convert_to_base64(
            "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"),
            b'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t')


class Challenge2(Set1TestCase):

    def test_xor_nonhex(self):
        self.assertRaises(ValueError, challenge2.fixed_xor_hex, "this is not a hex string", "this is not a hex string")

    def test_xor_nonequal(self):
        self.assertRaises(ValueError, challenge2.fixed_xor_hex, "DEADBEEF", "DEADBEEFDEADBEEF")

    def test_xor(self):
        self.assertEqual(challenge2.fixed_xor_hex(
            "1c0111001f010100061a024b53535009181c", "686974207468652062756c6c277320657965"),
            bytearray.fromhex("746865206b696420646f6e277420706c6179"))


class Challenge3(Set1TestCase):

    def test_single_byte_xor(self):
        self.assertEqual(
            challenge3.single_byte_xor(
                bytes.fromhex("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"),
                88),
            b"Cooking MC\'s like a pound of bacon")

    def test_decrypt_single_byte(self):
        self.assertEqual(
            challenge3.decrypt_single_byte_xor("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"),
            b"Cooking MC's like a pound of bacon")


class Challenge4(Set1TestCase):

    def test_detect_single_byte_xor(self):
        self.assertEqual(challenge4.detect_single_byte_xor(), b"Now that the party is jumping\n")


class Challenge5(Set1TestCase):
    def test_repeating_key_xor(self):
        import binascii
        encrypted = challenge5.encrypt_repeating_key("""Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal""".encode("ascii"), "ICE")
        self.assertEqual(
            binascii.hexlify(encrypted),
            b'0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f')

    def test_roundtrip_repeating_key(self):
        original = """Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal"""
        encrypted = challenge5.encrypt_repeating_key(original.encode("ascii"), "ICE")
        decrypted = challenge5.encrypt_repeating_key(encrypted, "ICE")
        self.assertEqual(original, decrypted.decode("ascii"))


class Challenge6(Set1TestCase):

    def __with_article(self, function):
        return self.with_file('challenge6_test.txt', function)

    def test_roundtrip_repeating_key_file(self):
        def roundtrip(f):
            original = f.read()
            encrypted = challenge5.encrypt_repeating_key(original.encode("ascii"), "STOP")
            decrypted = challenge5.encrypt_repeating_key(encrypted, "STOP")
            self.assertEqual(original, decrypted.decode("ascii"))
        self.__with_article(roundtrip)

    def test_hamming_distance(self):
        self.assertEqual(
            challenge6.hamming_distance(
                "this is a test".encode('ascii'),
                "wokka wokka!!!".encode('ascii')),
            37)

    def test_find_key_size_short(self):
        encrypted = b'0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f'
        self.assertEqual(challenge6.find_key_size(encrypted) % 3, 0)

    def encrypt_file(self, key):
        return self.__with_article(lambda f: challenge5.encrypt_repeating_key(f.read().encode("ascii"), key))

    def generate_key_size_test(self, key):
        encrypted = self.encrypt_file(key)
        self.assertEqual(challenge6.find_key_size(encrypted) % len(key), 0)

    def test_find_key_size_1(self):
        self.generate_key_size_test("STOP")

    def test_find_key_size_2(self):
        self.generate_key_size_test("COLLABORATE")

    def test_find_key_size_3(self):
        self.generate_key_size_test("LISTEN")

    def generate_detect_repeating_xor_key_test(self, key):
        def break_xor(f):
            original = f.read()
            encrypted = challenge5.encrypt_repeating_key(original.encode("ascii"), key)
            decrypted = challenge6.break_repeating_xor_bytes(encrypted)
            self.assertEqual(original, decrypted.decode("ascii"))
        self.__with_article(break_xor)

    def test_break_repeating_xor_1(self):
        self.generate_detect_repeating_xor_key_test("vanwinkle")

    def test_break_repeating_xor_2(self):
        self.generate_detect_repeating_xor_key_test("BaBy")

    def test_repeating_xor_challenge(self):
        challenge6.break_repeating_xor()
        self.maxDiff = None
        self.assertEqual(challenge6.break_repeating_xor(), self.with_file('challenge6_answer.txt',
                                                                          lambda f: f.read().encode("ascii")))


class Challenge7(Set1TestCase):

    def test_aes_in_ecb_challenge(self):
        self.assertEqual(challenge7.decrypt_aes_in_cbc_challenge(), self.with_file('challenge7_answer.txt',
                                                                                   lambda f: f.read().encode("ascii")))


if __name__ == '__main__':
    unittest.main()
