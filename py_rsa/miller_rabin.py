"""
__author__ = "Filip Ilic"
__email__ = "filip.ilic@htl.rennweg.at"
__version__ = "1.0.0"
__copyright__ = "Copyright 2024"
__license__ = "GPL"
__status__ = "Development"
"""
import random

FIRST_100_PRIMES = [ 2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
        31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
        73, 79, 83, 89, 97, 101, 103, 107, 109, 113,
        127, 131, 137, 139, 149, 151, 157, 163, 167, 173,
        179, 181, 191, 193, 197, 199, 211, 223, 227, 229,
        233, 239, 241, 251, 257, 263, 269, 271, 277, 281,
        283, 293, 307, 311, 313, 317, 331, 337, 347, 349,
        353, 359, 367, 373, 379, 383, 389, 397, 401, 409,
        419, 421, 431, 433, 439, 443, 449, 457, 461, 463,
        467, 479, 487, 491, 499, 503, 509, 521, 523, 541]

def is_prime(number):
    """
    Teste die ersten 100 Primzahlen auf Primzahl.
    """
    for prime in FIRST_100_PRIMES:
        if number % prime == 0:
            return False

    return is_prim_millerrabin(number) == "probably prime"

def is_prim_millerrabin(number, iterations=20):
    """
    Teste die ersten 100 Primzahlen auf Primzahl mittels Miller-Rabin-Test. Mindestens 20 Iterationen.
    """
    pass

def generate_prime(bits):
    """
    Generiere eine Primzahl mit einer bestimmten Bitlänge.
    """
    while True:
        prime_candidate = random.getrandbits(bits)
        prime_candidate |=  (1 << (bits - 1)) | 1 # set the most significant bit and the least significant bit
        if is_prime(prime_candidate):
            return prime_candidate

if __name__ == '__main__':
