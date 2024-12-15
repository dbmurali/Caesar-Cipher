# Caesar Cipher Program 🔐

A simple implementation of the Caesar Cipher encryption and decryption algorithm. This program allows users to encode and decode messages using a specified shift value. The Caesar Cipher is a basic encryption technique where each letter in the text is shifted by a certain number of positions in the alphabet.

## Features ✨
- **Encode**: Encrypt a message using a shift number.
- **Decode**: Decrypt a previously encoded message.
- **Handles Special Characters**: Spaces and non-alphabetical characters remain unaffected by the shift.
- **User-Friendly Interface**: Easy-to-follow prompts and options to continue or exit the program.

## How It Works 🧩
The program takes an input string and a shift value, and based on the selected action (encode or decode), it applies the Caesar Cipher logic to shift the letters of the alphabet. 

- **Shift**: Each letter is moved by the shift value provided by the user.
- **Wrap Around**: If the shift goes past 'z', it wraps around back to 'a' (and vice versa for decoding).
- **Non-Alphabet Characters**: Any characters other than letters (like spaces, punctuation, etc.) remain unchanged.

## Requirements 📦:
- **Python 3.x**: This program is written in Python and is compatible with Python 3.x versions.
- **art.py**: The `art` module is used for displaying a logo at the start of the program. You will need to have the `art.py` file in the same directory as the main program.

## How to Run ▶️:
1. Clone or download the repository to your local machine.
2. Ensure you have Python 3.x installed on your computer.
3. Run the program by executing the following command in your terminal or command prompt:
   ```bash
   python caesar_cipher.py
