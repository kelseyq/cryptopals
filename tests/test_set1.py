__author__ = 'Kelsey Gilmore-Innis'

import unittest
from set1 import challenge1, challenge2, challenge3

class SetOneTests(unittest.TestCase):

    def test_convert_to_base64_nonhex(self):
        self.assertRaises(ValueError, challenge1.convert_to_base64, "this is not a hex string")

    def test_convert_to_base64(self):
        self.assertEqual(challenge1.convert_to_base64(
            "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"),
            b'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t')

    def test_xor_nonhex(self):
        self.assertRaises(ValueError, challenge2.fixed_xor_hex, "this is not a hex string", "this is not a hex string")

    def test_xor_nonequal(self):
        self.assertRaises(ValueError, challenge2.fixed_xor_hex, "DEADBEEF", "DEADBEEFDEADBEEF")

    def test_xor(self):
        self.assertEqual(challenge2.fixed_xor_hex(
            "1c0111001f010100061a024b53535009181c", "686974207468652062756c6c277320657965"),
            bytearray.fromhex("746865206b696420646f6e277420706c6179"))

    def test_single_byte_xor(self):
        self.assertEqual(
            challenge3.single_byte_xor("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736", 88),
                                        b"Cooking MC\'s like a pound of bacon")

    def test_decrypt_single_byte(self):
        self.assertEqual(
            challenge3.decrypt_single_byte("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"),
            88)

if __name__ == '__main__':
    unittest.main()