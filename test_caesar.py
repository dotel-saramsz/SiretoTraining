import unittest
import caesarcipher


class TestCaesarCipher(unittest.TestCase):
    def test_string_without_space(self):
        plaintext = 'hello'
        key = 2
        ciphertext = 'jgnnq'
        self.assertEqual(ciphertext, caesarcipher.encrypt(plaintext, key)) and self.assertEqual(plaintext, caesarcipher.decrypt(ciphertext, key))

    def test_string_with_spaces(self):
        plaintext = 'hello world'
        key = 2
        ciphertext = 'jgnnq yqtnf'
        self.assertEqual(ciphertext, caesarcipher.encrypt(plaintext, key)) and self.assertEqual(plaintext, caesarcipher.decrypt(ciphertext, key))

    def test_string_with_spaces_and_numbers(self):
        plaintext = 'hello world 12345'
        key = 2
        ciphertext = 'jgnnq yqtnf 12345'
        self.assertEqual(ciphertext, caesarcipher.encrypt(plaintext, key)) and self.assertEqual(plaintext, caesarcipher.decrypt(ciphertext, key))


if __name__ == '__main__':
    unittest.main()
