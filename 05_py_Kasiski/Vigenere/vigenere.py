"""
__author__ = "Filip Ilic"
__email__ = "filip.ilic@htl.rennweg.at"
__version__ = "1.0.0"
__copyright__ = "Copyright 2024"
__license__ = "GPL"
__status__ = "Development"
"""

from ..Caesar.caesar import Caesar


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
        "Ourzv, qos nynh lm jwy?"

        :param plaintext:
        :param key:
        :return:
        """

        if key is None:
            key = self.key

        key = key.lower()
        plaintext = plaintext.lower()
        ciphertext = ""
        caesar = Caesar()
        for i in range(len(plaintext)):
            ciphertext += caesar.encrypt(plaintext[i], key[i % len(key)])
        return ciphertext

    pass
