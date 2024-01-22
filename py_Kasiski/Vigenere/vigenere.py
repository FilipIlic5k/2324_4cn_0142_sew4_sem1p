"""
__author__ = "Filip Ilic"
__email__ = "filip.ilic@htl.rennweg.at"
__version__ = "1.0.0"
__copyright__ = "Copyright 2024"
__license__ = "GPL"
__status__ = "Development"
"""

from py_Kasiski.Caesar.caesar import Caesar


class Vigenere:
    """
    Vigenere cipher class.
    """

    def __init__(self, key: str = "a"):
        """
        Constructor.
        :param key: Key to use for encryption and decryption
        """
        self.key = key

    def encrypt (self, plaintext: str, key: str = None) -> str:
        """
        Encrypts the given plaintext with Vigenere and the given key.

        >>> vigenere = Vigenere("b"); vigenere.key
        'b'

        >>> vigenere2 = Vigenere("hugo");vigenere2.encrypt("Hallo, wie geht es dir?")
        'ourzvhcwlhmsontszhjwy'

        :param plaintext:
        :param key:
        :return:
        """

        if key is None:
            key = self.key

        key = key.lower()
        caesar = Caesar()
        plaintext = caesar.to_lowercase_letter_only(plaintext)
        return ''.join([caesar.encrypt(plaintext[i], key[i % len(key)]) for i in range(len(plaintext))])

    pass
