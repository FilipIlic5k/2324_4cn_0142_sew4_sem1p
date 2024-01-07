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
