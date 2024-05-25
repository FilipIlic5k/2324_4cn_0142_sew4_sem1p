"""
__author__ = "Filip Ilic"
__email__ = "filip.ilic@htl.rennweg.at"
__version__ = "1.0.0"
__copyright__ = "Copyright 2024"
__license__ = "GPL"
__status__ = "Development"
"""

import argparse
import sys

# Assuming the necessary classes are in a module named py_Kasiski within the same directory or properly installed
from py_Kasiski.Caesar.caesar import Caesar
from py_Kasiski.Vigenere.vigenere import Vigenere
from py_Kasiski.Kasiski.kasiski import Kasiski


def parse_args():
    parser = argparse.ArgumentParser(description='Crack Caesar and Vigenere encrypted files.')
    parser.add_argument('infile', type=str, help='File to be cracked')
    parser.add_argument('-c', '--cipher', choices=['caesar', 'c', 'vigenere', 'v'], required=True, help='Cipher to use')
    parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output, display more information')
    parser.add_argument('-q', '--quiet', action='store_true', help='Quiet mode, display only the key')
    return parser.parse_args()


def read_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"{filename}: No such file or directory")
        sys.exit(1)


def crack_caesar(text, verbose):
    kasiski = Kasiski(text)
    key = kasiski.crack_key(1)  # Assuming key length 1 for Caesar
    if verbose:
        print(f"Cracking Caesar-encrypted file: Key = {key}")
    else:
        print(key)


def crack_vigenere(text, verbose):
    kasiski = Kasiski(text)
    # Example assumes some method to predict key length, here we use a simple placeholder
    key_length_guess = 4  # Placeholder for actual key length determination logic
    key = kasiski.crack_key(key_length_guess)
    if verbose:
        print(f"Cracking Vigenere-encrypted file: Key = {key}")
    else:
        print(key)


def main():
    args = parse_args()
    text = read_file(args.infile)
    if args.cipher in ['caesar', 'c']:
        crack_caesar(text, args.verbose)
    elif args.cipher in ['vigenere', 'v']:
        crack_vigenere(text, args.verbose)


if __name__ == '__main__':
    main()
