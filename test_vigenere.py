import unittest
import vigenerecipher


class TestVigenereCipher(unittest.TestCase):
    def test_case1(self):
        plaintext = 'go to the nearest station'
        key = 'vigenere'
        ciphertext = 'bwzsglvrzixifxjxvbosa'
        self.assertEqual(ciphertext, vigenerecipher.encrypt(plaintext, key)) and self.assertEqual(plaintext, vigenerecipher.decrypt(ciphertext, key))

    def test_case2(self):
        plaintext = 'leave and let live'
        key = 'javascript'
        ciphertext = 'uevvwcelaxcldvw'
        self.assertEqual(ciphertext, vigenerecipher.encrypt(plaintext, key)) and self.assertEqual(plaintext, vigenerecipher.decrypt(ciphertext, key))


if __name__ == '__main__':
    unittest.main()
