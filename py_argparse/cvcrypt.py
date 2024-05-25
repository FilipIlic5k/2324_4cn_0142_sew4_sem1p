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

from py_Kasiski.Caesar.caesar import Caesar
from py_Kasiski.Vigenere.vigenere import Vigenere


def parse_args():
    """
    Parse command line arguments.
    :return: Parsed arguments
    """
    parser = argparse.ArgumentParser(description='Encrypt and decrypt files using Caesar and Vigenere ciphers.')
    parser.add_argument('infile', type=str, help='File to encrypt or decrypt')
    parser.add_argument('outfile', type=str, nargs='?', help='Destination file')
    parser.add_argument('-c', '--cipher', choices=['caesar', 'c', 'vigenere', 'v'], required=True, help='Cipher to use')
    parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    parser.add_argument('-q', '--quiet', action='store_true', help='Quiet mode, suppress output')
    parser.add_argument('-d', '--decrypt', action='store_true', help='Decrypt the input')
    parser.add_argument('-e', '--encrypt', action='store_true', help='Encrypt the input')
    parser.add_argument('-k', '--key', type=str, required=True, help='Encryption key')
    return parser.parse_args()


def main():
    """
    Main function.
    """
    args = parse_args()
    cipher = Caesar() if args.cipher in ['caesar', 'c'] else Vigenere()

    try:
        with open(args.infile, 'r') as f:
            plaintext = f.read()
        if args.decrypt:
            crypttext = cipher.decrypt(plaintext, args.key)
        else:
            crypttext = cipher.encrypt(plaintext, args.key)

        with open(args.outfile, 'w') as f:
            f.write(crypttext)

        if args.verbose:
            print(
                f"{'Decrypting' if args.decrypt else 'Encrypting'} {args.cipher.title()} with key = {args.key} from file {args.infile} into file {args.outfile or args.infile}")

    except FileNotFoundError:
        print(f"{args.infile}: No such file or directory", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
