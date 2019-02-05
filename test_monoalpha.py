import unittest
import monoalphabetic


class TestMonoalphabeticCipher(unittest.TestCase):
    def test_string_without_space(self):
        plaintext = 'defendtheeastwallofthecastle'
        key = 'qmrhsnxbwpgjauoecklfzyvtdi'
        ciphertext = 'hsnsuhfbssqlfvqjjonfbsrqlfjs'
        self.assertEqual(ciphertext, monoalphabetic.encrypt(plaintext, key)) and self.assertEqual(plaintext, monoalphabetic.decrypt(ciphertext, key))

    def test_string_with_spaces(self):
        plaintext = 'defend the east wall of the castle'
        key = 'qmrhsnxbwpgjauoecklfzyvtdi'
        ciphertext = 'hsnsuh fbs sqlf vqjj on fbs rqlfjs'
        self.assertEqual(ciphertext, monoalphabetic.encrypt(plaintext, key)) and self.assertEqual(plaintext, monoalphabetic.decrypt(ciphertext, key))

    def test_string_with_spaces_and_numbers(self):
        plaintext = 'defend the east wall of the castle 12345'
        key = 'qmrhsnxbwpgjauoecklfzyvtdi 12345'
        ciphertext = 'hsnsuh fbs sqlf vqjj on fbs rqlfjs 12345'
        self.assertEqual(ciphertext, monoalphabetic.encrypt(plaintext, key)) and self.assertEqual(plaintext, monoalphabetic.decrypt(ciphertext, key))


if __name__ == '__main__':
    unittest.main()
