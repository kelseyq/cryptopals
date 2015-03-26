__author__ = 'Kelsey Gilmore-Innis'

import unittest
from set_one import challenge_one

class SetOneTests(unittest.TestCase):

    def test_convert_to_base64_nonhex(self):
        self.assertRaises(ValueError, challenge_one.convert_to_base64, "this is not a hex string")

    def test_convert_to_base64(self):
        self.assertEqual(challenge_one.convert_to_base64(
            "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"),
            b'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t')

if __name__ == '__main__':
    unittest.main()