"""
__author__ = "Filip Ilic"
__email__ = "filip.ilic@htl.rennweg.at"
__version__ = "1.0.0"
__copyright__ = "Copyright 2024"
__license__ = "GPL"
__status__ = "Development"
"""


class Caesar:
    """
    Caesar cipher class.
    """

    def __init__(self, key: int = 1):
        """
        Constructor.
        :param key: Key to use for encryption and decryption
        """
        self.key = key


    def to_lowercase_letter_only(self, plaintext: str) -> str:
        """
        Returns the plaintext in lowercase and without special characters.

        >>> caesar1 = Caesar(); caesar1.to_lowercase_letter_only("Hallo, wie geht es dir?")
        'hallowiegehtesdir'

        :param plaintext:
        :return:
        """

        return "".join([c for c in plaintext.lower() if c.isalpha()])

    def encrypt(self, plaintext: str, key:str = None) -> str:
        """
        Encrypts the given plaintext with the given key.
        :param plaintext:
        :param key: is a letter that defines how many letters the alphabet is shifted
        if no key is given, the default key is taken by the property
        :return:

        >>> caesar=Caesar("b"); caesar.key
        'b'

        >>> caesar2 = Caesar();caesar2.encrypt("hallo")
        'ibmmp'

        >>> caesar3 = Caesar();caesar3.decrypt("ibmmp")
        'hallo'

        >>> caesar4 = Caesar();caesar4.encrypt("hallo", "c")
        'jcnnq'

        >>> caesar5 = Caesar();caesar5.encrypt("xyz", "c")
        'zab'
        """
        if key is None:
            key = self.key
        elif isinstance(key, str) and len(key) == 1 and key.islower():
            key = ord(key) - ord('a')
        elif not isinstance(key, int):
            raise ValueError("Key must be an integer or a single lowercase letter.")

        plaintext = self.to_lowercase_letter_only(plaintext)
        ciphertext = ""
        for c in plaintext:
            ciphertext += chr((ord(c) - ord('a') + key) % 26 + ord('a'))
        return ciphertext

    def decrypt(self, ciphertext: str, key:str = None) -> str:
        """
        Decrypts the given ciphertext with the given key.

        :param ciphertext:
        :param key: is a letter that defines how many letters the alphabet is shifted
        if no key is given, the default key is taken by the property
        :return:
        """
        if key is None:
            key = self.key
        elif isinstance(key, str) and len(key) == 1 and key.islower():
            key = ord(key) - ord('a')
        elif not isinstance(key, int):
            raise ValueError("Key must be an integer or a single lowercase letter.")

        ciphertext = self.to_lowercase_letter_only(ciphertext)
        plaintext = ""
        for c in ciphertext:
            plaintext += chr((ord(c) - ord('a') - key) % 26 + ord('a'))
        return plaintext

    pass
