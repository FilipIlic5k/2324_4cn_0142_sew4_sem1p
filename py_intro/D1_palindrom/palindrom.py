"""
__author__ = "Filip Ilic"
__email__ = "filip.ilic@htl.rennweg.at"
__version__ = "1.0.0"
__copyright__ = "Copyright 2024"
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


def is_palindrom_sentence(s: str):
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

    >>> million = palindrom_product(1_000_000); million
    0

    :param x: input number
    :return: biggest palindrome product
    """
    n = 0
    for i in range(x, 0, -1):
        for j in range(i, 0, -1):
            x = i * j
            if x > n:
                if is_palindrom(str(x)):
                    n = x
    return n


import string

DIGITS = string.digits + string.ascii_uppercase


def to_base(number: int, base: int) -> str:
    """
    Converts a number from decimal to a given base.

    >>> num0 = to_base(1234,16); num0
    '4D2'

    >>> num1 = to_base(10, 2); num1
    '1010'

    >>> num2 = to_base(10, 3); num2
    '101'

    >>> num3 = to_base(10, 4); num3
    '22'

    >>> num4 = to_base(10, 5); num4
    '20'

    >>> num5= to_base(10, 11); num5
    'A'

    >>> num6 = to_base (1_000_000, 128); num6
    'x'

    :param number: Number in 10-base system
    :param base: Base to convert to
    :return: Number converted to given base
    """
    if number < 0:
        sign = -1
    elif number == 0:
        return DIGITS[0]
    else:
        sign = 1

    number *= sign
    digits = []

    while number:
        digits.append(DIGITS[number % base])
        #number = number // base
        number //= base

    if sign < 0:
        digits.append('-')

    return ''.join(digits[::-1])


def get_dec_hex_palindrom(x):
    """
    Gets the biggest number (smaller than x), that is a palindrom in the decimal system and the hexadecimal system.

    >>> num1 = get_dec_hex_palindrom(1_000); num1
    (979, '3D3')

    >>> num2 = get_dec_hex_palindrom(5_000_000); num2
    (2485842, '25EE52')

    >>> num3 = get_dec_hex_palindrom(1_000_000); num3
    x

    :param x: input number
    :return: biggest palindrome number
    """
    n = 0
    for i in range(x, 0, -1):
        if is_palindrom(str(i)) and is_palindrom(to_base(i, 16)):
            n = i
            break
    return n, to_base(n, 16)
