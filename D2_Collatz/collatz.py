from typing import List


def collatz(n):
    """
    Return the next number in the Collatz sequence.
    :param n: Number to start the sequence from
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
        return 3 * n + 1



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
