#!/usr/bin/env python3
import sys
import logging
import string
from collections import Counter

ALPHABET = string.ascii_lowercase
ENGLISH_FREQ_ORDER = "etaoinshrdlcumwfgypbvkjxqz"


def caesar_shift_char(c, shift):
    if c.isalpha():
        base = ord('a') if c.islower() else ord('A')
        return chr((ord(c) - base + shift) % 26 + base)
    return c


def caesar(text, shift):
    return "".join(caesar_shift_char(c, shift) for c in text)


def encrypt(text, shift):
    return caesar(text, shift)


def decrypt(text, shift):
    return caesar(text, -shift)


def score_english(text):
    """
    Rough English-likeness score using letter frequency.
    Lower score is better.
    """
    text = text.lower()
    letters = [c for c in text if c in ALPHABET]
    if not letters:
        return float("inf")

    freq = Counter(letters)
    total = sum(freq.values())

    score = 0
    for letter in ALPHABET:
        observed = freq.get(letter, 0) / total
        expected = (26 - ENGLISH_FREQ_ORDER.index(letter)) / 351
        score += abs(observed - expected)

    return score


def break_cipher(ciphertext):
    candidates = []
    for shift in range(26):
        plaintext = decrypt(ciphertext, shift)
        score = score_english(plaintext)
        candidates.append((score, shift, plaintext))

    candidates.sort()
    logging.debug(candidates)
    return candidates[0]  # best guess


def usage():
    print("Usage:")
    print("  python monoalphabetic.py encrypt <shift> <text>")
    print("  python monoalphabetic.py decrypt <shift> <text>")
    print("  python monoalphabetic.py break <ciphertext>")
    sys.exit(1)


def main():
    if len(sys.argv) < 3:
        usage()

    mode = sys.argv[1].lower()

    if mode == "encrypt":
        if len(sys.argv) < 4:
            usage()
        shift = int(sys.argv[2])
        text = " ".join(sys.argv[3:])
        print(encrypt(text, shift))

    elif mode == "decrypt":
        if len(sys.argv) < 4:
            usage()
        shift = int(sys.argv[2])
        text = " ".join(sys.argv[3:])
        print(decrypt(text, shift))

    elif mode == "break":
        text = " ".join(sys.argv[2:])
        score, shift, plaintext = break_cipher(text)
        print(f"[+] Best shift: {shift}")
        print(f"[+] Plaintext: {plaintext}")

    else:
        usage()


if __name__ == "__main__":
    main()

