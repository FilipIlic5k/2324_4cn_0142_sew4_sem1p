"""
__author__ = "Filip Ilic"
__email__ = "filip.ilic@htl.rennweg.at"
__version__ = "1.0.0"
__copyright__ = "Copyright 2024"
__license__ = "GPL"
__status__ = "Development"
"""

import itertools
import time


def is_prime(n):
    """
    Function that checks if a number is prime
    :param n: number to check
    :return: True if n is prime, False otherwise

    >>> is_prime(2)
    True
    >>> is_prime(3)
    True
    >>> is_prime(4)
    False
    >>> is_prime(174440041)
    True
    >>> is_prime(174440042)
    False
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(pow(n, 0.5)) + 1, 2):
        if n % i == 0:
            return False
    return True


def primes():
    """
    Generator function that generates prime numbers
    :return: prime number

    >>> p = primes()
    >>> next(p)
    2
    """
    yield 2
    n = 3
    while True:
        if is_prime(n):
            yield n
        n += 2


if __name__ == "__main__":
    import doctest
    doctest.testmod()

    # Die ersten 100 Primzahlen ausgeben
    print(list(itertools.islice(primes(), 100)))

    # Alle Primzahlen bis 100 000 ausgeben
    print(list(itertools.takewhile(lambda x: x < 100000, primes())))

    # Wie lange braucht man zum Bestimmen der 200.000-ten Primzahl? 400.000-te?
    start = time.time()
    prime_200000 = next(itertools.islice(primes(), 199999, None))
    end = time.time()
    print("200.000-te Primzahl:", prime_200000, "benötigte Zeit:", end - start)

    start2 = time.time()
    prime_400000 = next(itertools.islice(primes(), 399999, None))
    end2 = time.time()
    print("400.000-te Primzahl:", prime_400000, "benötigte Zeit:", end2 - start2)
