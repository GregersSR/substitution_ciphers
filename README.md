# Substitution Ciphers

This repository contains Python implementations of classic **substitution ciphers**:

- **Monoalphabetic (Caesar) cipher**  
- **Polyalphabetic (Vigenère) cipher**  

It supports **encryption**, **decryption**, and **automatic breaking** using frequency analysis.

---

## Features

### Monoalphabetic (`monoalphabetic.py`)
- Encrypt/decrypt text using a single shift (Caesar cipher)  
- Automatic breaking of Caesar cipher via frequency analysis  
- Preserves:
  - Uppercase and lowercase letters  
  - Punctuation and spaces  

### Polyalphabetic (`polyalphabetic.py`)
- Encrypt/decrypt text using an arbitrary alphabetic key (Vigenère cipher)  
- Automatic breaking of short Vigenère ciphers using frequency analysis  
- Fully case-preserving  
- Preserves punctuation and spaces  

---

## Installation

No dependencies beyond **Python 3**.

Clone the repository:

```bash
git clone <repository_url>
cd substitution_ciphers
```

Make scripts executable (optional):

```bash
chmod +x monoalphabetic.py polyalphabetic.py
```

---

## Usage

### Monoalphabetic / Caesar cipher

Encrypt:

```bash
python monoalphabetic.py encrypt <shift> "<text>"
# Example
python monoalphabetic.py encrypt 3 "Hello World"
```

Decrypt:

```bash
python monoalphabetic.py decrypt <shift> "<ciphertext>"
```

Break:

```bash
python monoalphabetic.py break "<ciphertext>"
```

### Polyalphabetic / Vigenère cipher

Encrypt:

```bash
python polyalphabetic.py encrypt <key> "<text>"
# Example
python polyalphabetic.py encrypt SECRET "Hello World"
```

Decrypt:

```bash
python polyalphabetic.py decrypt <key> "<ciphertext>"
```

Break:

```bash
python polyalphabetic.py break "<ciphertext>"
```

> Note: Automatic breaking works best on reasonably long English text.

---

## Running Tests

Unit tests are included for both ciphers:

```bash
# Monoalphabetic
python -m unittest test_monoalphabetic.py

# Polyalphabetic
python -m unittest test_polyalphabetic.py
```

> Tests check correctness of encryption, decryption, and breaking functionality.

---

## Implementation Notes

- **Monoalphabetic** is implemented as a **special case of polyalphabetic** with a one-letter key.  
- **Breaking** uses **frequency analysis** and chi-squared scoring.  
- Text case and non-alphabetic characters are preserved in all operations.  

---

## Limitations

- Polyalphabetic breaking is heuristic:
  - Works reliably for **long ciphertexts**  
  - May fail or produce approximate results for **short or highly irregular text**  
- No support for non-English character sets.  

---

## License

MIT License — free to use, modify, and distribute.

