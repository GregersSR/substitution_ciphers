import logging
import unittest
import monoalphabetic


class TestMonoalphabeticCipher(unittest.TestCase):

    def test_encrypt_basic(self):
        self.assertEqual(
            monoalphabetic.encrypt("abc", 3),
            "def"
        )

    def test_encrypt_wraparound(self):
        self.assertEqual(
            monoalphabetic.encrypt("xyz", 3),
            "abc"
        )

    def test_encrypt_preserves_case(self):
        self.assertEqual(
            monoalphabetic.encrypt("Hello World", 3),
            "Khoor Zruog"
        )

    def test_encrypt_non_alpha(self):
        self.assertEqual(
            monoalphabetic.encrypt("Hello, World!", 3),
            "Khoor, Zruog!"
        )

    def test_decrypt_basic(self):
        self.assertEqual(
            monoalphabetic.decrypt("def", 3),
            "abc"
        )

    def test_decrypt_wraparound(self):
        self.assertEqual(
            monoalphabetic.decrypt("abc", 3),
            "xyz"
        )

    def test_encrypt_decrypt_inverse(self):
        plaintext = "Attack at dawn!"
        shift = 7
        ciphertext = monoalphabetic.encrypt(plaintext, shift)
        decrypted = monoalphabetic.decrypt(ciphertext, shift)
        self.assertEqual(decrypted, plaintext)

    def test_break_simple_cipher(self):
        plaintext = "This is a simple test message. The length has been increased such that it is long enough to break."
        shift = 5
        ciphertext = monoalphabetic.encrypt(plaintext, shift)

        score, recovered_shift, recovered_text = monoalphabetic.break_cipher(ciphertext)

        self.assertEqual(recovered_shift, shift)
        self.assertEqual(recovered_text, plaintext)

    def test_break_with_mixed_case(self):
        plaintext = "Hello World is a classic phrase in programming. It serves as demonstration that some text can be printed."
        shift = 3
        ciphertext = monoalphabetic.encrypt(plaintext, shift)

        _, recovered_shift, recovered_text = monoalphabetic.break_cipher(ciphertext)

        self.assertEqual(recovered_shift, shift)
        self.assertEqual(recovered_text, plaintext)

    def test_empty_string(self):
        self.assertEqual(monoalphabetic.encrypt("", 5), "")
        self.assertEqual(monoalphabetic.decrypt("", 5), "")


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    unittest.main()

