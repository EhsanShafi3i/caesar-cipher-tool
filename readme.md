# Caesar Cipher Cryptanalysis Tool

A Python-based cryptographic tool that implements the Caesar Cipher along with various cryptanalysis methods for educational purposes.

## Features

### Encryption/Decryption
- Basic Caesar cipher encryption
- Decryption with known key
- Support for both letters and numbers
- Case preservation

### Cryptanalysis Methods
- Brute Force Attack
- Frequency Analysis 
- Known Word Attack
- Transposition Attack
- Anagram Attack

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ehsanshfi3i/caesar-cipher-tool.git
   ```

2. Navigate to the project directory:
   ```bash
   cd caesar-cipher-tool
   ```

3. Run the script:
   ```bash
   python caesarcipher.py
   ```

## Usage

### Basic Operations

1. **Encryption**
   - Choose 'E' when prompted
   - Enter shift number (0-25)
   - Enter text to encrypt

2. **Decryption with Known Key**
   - Choose 'D' when prompted
   - Enter decryption key
   - Enter encrypted text

### Advanced Cryptanalysis

Choose 'W' for cryptanalysis options:

- **Brute Force (B)**: Tests all 26 possible shifts
- **Frequency Analysis (F)**: Analyzes letter frequencies
- **Known Word Attack (K)**: Searches for common words
- **Transposition Attack (T)**: Tests character shifts
- **Anagram Attack (A)**: Analyzes word rearrangements

## Technical Details

- Written in Python 3
- Uses modular arithmetic for shifting
- Preserves non-alphabetic characters
- Handles both uppercase and lowercase
- Includes number shifting (0-9)

## Dependencies

- Python 3.x
- Standard Library:
  - `string`
  - `collections.Counter`

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Disclaimer

This tool is for educational purposes only. For real-world applications, please use modern cryptographic standards.

## Contact

Your Name - [@EHSANSHAFI3I](https://x.com/EHSANSHAFI3I)

Project Link: [https://github.com/ehsanshafi3i/caesar-cipher-tool](https://github.com/ehsanshafi3i/caesar-cipher-tool)

# Explanation of Decryption Methods

This document provides a detailed explanation of each decryption method implemented in the Caesar Cipher Cryptanalysis Tool.

## Decryption Methods

### 1. Brute Force Attack

**Description:**
The brute force attack method systematically tries all possible keys (0-25) to decrypt the text. Since the Caesar Cipher has a limited key space, this method is feasible and guarantees finding the correct decryption.

**How it Works:**
- Iterate over all possible key values from 0 to 25.
- For each key, shift the letters in the encrypted text backward by the key value.
- Output all possible decrypted texts for analysis.

### 2. Frequency Analysis

**Description:**
Frequency analysis exploits the fact that certain letters appear more frequently in a language. In English, 'E' is the most common letter. By identifying the most frequent letter in the encrypted text, we can estimate the key.

**How it Works:**
- Count the frequency of each letter in the encrypted text.
- Identify the most common letter.
- Assume this letter corresponds to 'E' and calculate the key.
- Use the key to decrypt the text.

### 3. Known Word Attack

**Description:**
This method assumes that a specific word (e.g., "THE") is present in the plaintext. By finding where this word could fit in the encrypted text, we can deduce the key.

**How it Works:**
- Choose a common word expected in the plaintext.
- Slide this word across the encrypted text to find potential matches.
- Calculate the key based on the alignment of the known word with the encrypted text.
- Decrypt the text using the identified key.

### 4. Transposition Attack

**Description:**
The transposition attack is not directly applicable to the Caesar Cipher but is included for educational purposes. It involves rearranging the characters in the text to find a meaningful message.

**How it Works:**
- Test different character shifts (transpositions) across the text.
- For each shift, rearrange the text and check for meaningful output.
- Output all possible transpositions for analysis.

### 5. Anagram Attack

**Description:**
An anagram attack involves rearranging the letters of words in the encrypted text to form meaningful words. This method is more relevant to substitution ciphers but can be explored with Caesar Cipher for educational purposes.

**How it Works:**
- Split the encrypted text into words.
- Generate all possible anagrams for each word.
- Check if any anagram forms a meaningful word or phrase.
- Output possible anagrams for analysis.

## Conclusion

Each decryption method offers a unique approach to breaking the Caesar Cipher. While some methods like brute force are guaranteed to work, others like frequency analysis and known word attack rely on linguistic patterns and assumptions. These methods provide a comprehensive toolkit for understanding and breaking simple substitution ciphers.
