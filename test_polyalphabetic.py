import unittest
import polyalphabetic


class TestPolyalphabeticCipher(unittest.TestCase):

    def test_encrypt_basic(self):
        self.assertEqual(
            polyalphabetic.encrypt("ATTACKATDAWN", "LEMON"),
            "LXFOPVEFRNHR"
        )

    def test_decrypt_basic(self):
        self.assertEqual(
            polyalphabetic.decrypt("LXFOPVEFRNHR", "LEMON"),
            "ATTACKATDAWN"
        )

    def test_preserves_case_and_punctuation(self):
        plaintext = "Hello, World!"
        key = "KEY"
        cipher = polyalphabetic.encrypt(plaintext, key)
        decrypted = polyalphabetic.decrypt(cipher, key)
        self.assertEqual(decrypted, plaintext)

    def test_encrypt_decrypt_inverse(self):
        plaintext = "This is a longer test message for vigenere cipher"
        key = "crypto"
        cipher = polyalphabetic.encrypt(plaintext, key)
        self.assertEqual(
            polyalphabetic.decrypt(cipher, key),
            plaintext
        )

    def test_empty_key_raises(self):
        with self.assertRaises(ValueError):
            polyalphabetic.encrypt("test", "123")

    def test_break_cipher(self):
        plaintext = (
            "this is a reasonably long english text "
            "used to test the breaking of vigenere cipher"
        )
        key = "secret"
        cipher = polyalphabetic.encrypt(plaintext, key)

        score, recovered_key, recovered_text = polyalphabetic.break_cipher(cipher)

        self.assertEqual(recovered_text, plaintext)
        self.assertEqual(recovered_key, key)

    def test_break_short_text_fails(self):
        with self.assertRaises(ValueError):
            polyalphabetic.break_cipher("ABC")


if __name__ == "__main__":
    unittest.main()

