"""
__author__ = "Filip Ilic"
__email__ = "filip.ilic@htl.rennweg.at"
__version__ = "1.0.0"
__copyright__ = "Copyright 2023"
__license__ = "GPL"
__status__ = "Development"
"""


def is_palindrom(s: str):
    """
    Checks if a string is a palindrom.
    A palindrom is a string that is the same when read backwards.

    >>> str1 = is_palindrom("anna"); str1
    True

    >>> str2 = is_palindrom(" anna"); str2
    True

    >>> str3 = is_palindrom("lotto"); str3
    False

    :param s: input string
    :return: boolean
    """
    s = s.replace(" ", "").lower()
    return s == s[::-1]

def is_palindrom_sentence(s:str):
    """
    Checks if a string is a palindrom.
    A palindrom is a string that is the same when read backwards.

    >>> str1 = is_palindrom_sentence("Oh, Chello! Voll Ehco!"); str1
    False

    >>> str2 = is_palindrom_sentence("Oh, Chello! Voll Ehcho!"); str2
    True

    >>> str3 = is_palindrom_sentence("Eine Horde bedrohe nie!"); str3
    True

    >>> str4 = is_palindrom_sentence("O Genie, der Mann ehre dein Ego!"); str4
    False

    :param s: input string
    :return: boolean
    """
    s = s.replace(" ", "").replace(",", "").replace("!", "").replace("?", "").replace(".", "").lower()
    return is_palindrom(s)