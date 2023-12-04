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

def palindrom_product(x):
    """
    Gets the biggest number (smaller that x), that is the product of 2 3-digit numbers.

    >>> num1 = palindrom_product(1000); num1
    906609

    >>> num2 = palindrom_product(100); num2
    9009

    >>> num3 = palindrom_product(10); num3
    9

    >>> num_insane = palindrom_product(10_000); num_insane
    99000099

    :param x: input number
    :return: biggest palindrome number
    """
    n = 0
    for i in range(x, 0, -1):
        for j in range(i, 0, -1):
            x = i * j
            if x > n:
                if is_palindrom(str(i * j)):
                    n = i * j
    return n