#!/usr/bin/env python3
import sys
import string
from collections import Counter

ALPHABET = string.ascii_lowercase
ENGLISH_FREQ = {
    'a': 0.08167, 'b': 0.01492, 'c': 0.02782, 'd': 0.04253,
    'e': 0.12702, 'f': 0.02228, 'g': 0.02015, 'h': 0.06094,
    'i': 0.06966, 'j': 0.00153, 'k': 0.00772, 'l': 0.04025,
    'm': 0.02406, 'n': 0.06749, 'o': 0.07507, 'p': 0.01929,
    'q': 0.00095, 'r': 0.05987, 's': 0.06327, 't': 0.09056,
    'u': 0.02758, 'v': 0.00978, 'w': 0.02360, 'x': 0.00150,
    'y': 0.01974, 'z': 0.00074,
}


def clean_key(key):
    return "".join(c.lower() for c in key if c.isalpha())


def shift_char(c, shift):
    base = ord('a') if c.islower() else ord('A')
    return chr((ord(c) - base + shift) % 26 + base)


def vigenere(text, key, decrypt=False):
    key = clean_key(key)
    if not key:
        raise ValueError("Key must contain alphabetic characters")

    result = []
    ki = 0

    for c in text:
        if c.isalpha():
            shift = ord(key[ki % len(key)]) - ord('a')
            if decrypt:
                shift = -shift
            result.append(shift_char(c, shift))
            ki += 1
        else:
            result.append(c)

    return "".join(result)


def encrypt(text, key):
    return vigenere(text, key, decrypt=False)


def decrypt(text, key):
    return vigenere(text, key, decrypt=True)


def chi_squared(text):
    text = [c for c in text.lower() if c in ALPHABET]
    if not text:
        return float("inf")

    freq = Counter(text)
    n = len(text)

    score = 0
    for letter in ALPHABET:
        observed = freq.get(letter, 0)
        expected = ENGLISH_FREQ[letter] * n
        score += (observed - expected) ** 2 / expected

    return score


def best_caesar_shift(text):
    scores = []
    for shift in range(26):
        decrypted = "".join(
            shift_char(c, -shift) if c.isalpha() else c for c in text
        )
        scores.append((chi_squared(decrypted), shift))
    return min(scores)[1]


def break_cipher(ciphertext, max_key_length=10):
    letters_only = [c for c in ciphertext if c.isalpha()]
    if len(letters_only) < 20:
        raise ValueError("Ciphertext too short to break")

    best_result = None

    for key_len in range(1, max_key_length + 1):
        key = ""
        for i in range(key_len):
            slice_i = "".join(
                letters_only[j]
                for j in range(i, len(letters_only), key_len)
            )
            shift = best_caesar_shift(slice_i)
            key += chr(ord('a') + shift)

        plaintext = decrypt(ciphertext, key)
        score = chi_squared(plaintext)

        if best_result is None or score < best_result[0]:
            best_result = (score, key, plaintext)

    return best_result


def usage():
    print("Usage:")
    print("  python polyalphabetic.py encrypt <key> <text>")
    print("  python polyalphabetic.py decrypt <key> <text>")
    print("  python polyalphabetic.py break <ciphertext>")
    sys.exit(1)


def main():
    if len(sys.argv) < 3:
        usage()

    mode = sys.argv[1].lower()

    if mode == "encrypt":
        if len(sys.argv) < 4:
            usage()
        key = sys.argv[2]
        text = " ".join(sys.argv[3:])
        print(encrypt(text, key))

    elif mode == "decrypt":
        if len(sys.argv) < 4:
            usage()
        key = sys.argv[2]
        text = " ".join(sys.argv[3:])
        print(decrypt(text, key))

    elif mode == "break":
        text = " ".join(sys.argv[2:])
        score, key, plaintext = break_cipher(text)
        print(f"[+] Key: {key}")
        print(f"[+] Plaintext: {plaintext}")

    else:
        usage()


if __name__ == "__main__":
    main()

