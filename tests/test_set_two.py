__author__ = 'Kelsey Gilmore-Innis'

import unittest
from set_one import challenge_two

class SetTwoTests(unittest.TestCase):

    def test_xor_nonhex(self):
        self.assertRaises(ValueError, challenge_two.fixed_xor, "this is not a hex string", "this is not a hex string")

    def test_xor_nonequal(self):
        self.assertRaises(ValueError, challenge_two.fixed_xor, "DEADBEEF", "DEADBEEFDEADBEEF")

    def test_xor(self):
        self.assertEqual(challenge_two.fixed_xor(
            "1c0111001f010100061a024b53535009181c", "686974207468652062756c6c277320657965"),
            bytearray.fromhex("746865206b696420646f6e277420706c6179"))

if __name__ == '__main__':
    unittest.main()