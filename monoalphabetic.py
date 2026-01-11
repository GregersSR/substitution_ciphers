#!/usr/bin/env python3
import sys
import polyalphabetic


def shift_to_key(shift):
    return chr(ord('a') + (shift % 26))


def encrypt(text, shift):
    key = shift_to_key(shift)
    return polyalphabetic.encrypt(text, key)


def decrypt(text, shift):
    key = shift_to_key(shift)
    return polyalphabetic.decrypt(text, key)


def break_cipher(ciphertext):
    score, key, plaintext = polyalphabetic.break_cipher(ciphertext, max_key_length=1)
    shift = ord(key[0]) - ord('a')
    return score, shift, plaintext


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
        shift = int(sys.argv[2])
        text = " ".join(sys.argv[3:])
        print(encrypt(text, shift))

    elif mode == "decrypt":
        shift = int(sys.argv[2])
        text = " ".join(sys.argv[3:])
        print(decrypt(text, shift))

    elif mode == "break":
        text = " ".join(sys.argv[2:])
        score, shift, plaintext = break_cipher(text)
        print(f"[+] Shift: {shift}")
        print(f"[+] Plaintext: {plaintext}")

    else:
        usage()


if __name__ == "__main__":
    main()

