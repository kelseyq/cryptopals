__author__ = 'Kelsey Gilmore-Innis'

import unittest
from set1 import challenge1, challenge2, challenge3, challenge4, challenge5

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
            challenge3.decrypt_single_byte_xor("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"),
            "Cooking MC's like a pound of bacon")

    def test_detect_single_byte_xor(self):
        self.assertEqual(challenge4.detect_single_byte_xor(), "Now that the party is jumping\n")

    def test_repeating_key_xor(self):
        self.assertEqual(challenge5.encrypt_repeating_key("""Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal""", "ICE"), b'0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f')

if __name__ == '__main__':
    unittest.main()