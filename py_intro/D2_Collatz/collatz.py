"""
__author__ = "Filip Ilic"
__email__ = "filip.ilic@htl.rennweg.at"
__version__ = "1.0.0"
__copyright__ = "Copyright 2024"
__license__ = "GPL"
__status__ = "Development"
"""


from typing import List


def collatz(n,p:int=3):
    """
    Return the next number in the Collatz sequence.
    :param n: Number to start the sequence from
    :param p: Number to stop the sequence
    :return: Next number in the Collatz sequence

    >>> c1 = collatz(25); c1
    76
    >>> c2 = collatz(76); c2
    38
    >>> c3 = collatz(38); c3
    19
    >>> c4 = collatz(-19); c4
    Traceback (most recent call last):
    ...
    ValueError: n must be a positive integer
    """

    if n < 0:
        raise ValueError("n must be a positive integer")

    if n % 2 == 0:
        return n // 2

    if n % 2 != 0:
        return p * n + 1



def collatz_sequence(number:int)->List[int]:
    """
    Return the Collatz sequence from a given number.

    >>> cs1 = collatz_sequence(19); cs1
    [19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]

    >>> cs2 = collatz_sequence(21); cs2
    [21, 64, 32, 16, 8, 4, 2, 1]

    >>> cs3 = collatz_sequence(18); cs3
    [18, 9, 28, 14, 7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]

    >>> cs4 = collatz_sequence(-19); cs4
    Traceback (most recent call last):
    ...
    ValueError: n must be a positive integer

    :param number: Number to start the sequence from
    :return: Collatz sequence
    """

    if number < 0:
        raise ValueError("n must be a positive integer")

    sequence = [number]

    while number != 1:
        number = collatz(number)
        sequence.append(number)

    return sequence


def longest_collatz_sequence(n: int) -> tuple[int, int]:
    """
    Return the longest Collatz sequence length and the starting number under a given number.

    >>> lcs1 = longest_collatz_sequence(100); lcs1
    (97, 119)

    >>> lcs2 = longest_collatz_sequence(1_000); lcs2
    (871, 179)

    >>> lcs20k = longest_collatz_sequence(20_000); lcs20k
    (871, 179)

    >>> lcs3 = longest_collatz_sequence(-1_000); lcs3
    Traceback (most recent call last):
    ...
    ValueError: n must be a positive integer

    :param n: Number to check under
    :return: Startnumber and Length of the longest Collatz sequence with the startnumber <=n
    """
    longest = 0
    startnumber = 0

    if n < 0:
        raise ValueError("n must be a positive integer")

    for i in range(1, n + 1):
        length = len(collatz_sequence(i))
        if length > longest:
            longest = length
            startnumber = i

    return startnumber, longest


