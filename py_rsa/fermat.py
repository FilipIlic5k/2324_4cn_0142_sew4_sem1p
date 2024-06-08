"""
__author__ = "Filip Ilic"
__email__ = "filip.ilic@htl.rennweg.at"
__version__ = "1.0.0"
__copyright__ = "Copyright 2024"
__license__ = "GPL"
__status__ = "Development"
"""
from collections import Counter

"""
Berechne (in Python) für jede der Primzahlen p = 2 bis p = 11 und p = 997:
• für jeweils jedes Element a (ohne 0) von Zp (d.h. Restklasse p bzw. ... mod p, a = 1...p − 1
– den Wert ap−1 in Zp .
"""


def fermat(p):
    """
    Kleiner Fermatischer Satz.
    Berechnet für jede Primzahl p den Wert von a^(p-1) mod p für a = 1...p-1
    :param p: Primzahl
    """
    return [pow(a, p - 1, p) for a in range(1, p)]


def display(values, p):
    """
    Gibt die Werte von a^(p-1) mod p für a = 1...p-1 aus Für jede Primzahl p wird der Prozentsatz der 1en in der
    Liste ausgegeben welche die Wahrscheinlichkeit angibt, dass p eine Primzahl ist.

    :param values: Liste von Werten
    :param p: Primzahl :param
    """
    counter = Counter(values)
    total = len(values)
    percentage = (counter[1] / total) * 100 if 1 in counter else 0
    print(f"{p} -> {percentage:.2f} % -> res[1]={counter[1]},"
          f" len(res)={total} - {list(counter.items())}")


if __name__ == '__main__':
    primes = list(range(2, 12)) + [997]
    non_primes = [9, 15, 21, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562,
                  563, 564, 565, 566, 567, 568, 569, 6601, 8911]

    print("Ergebnisse für Primzahlen von 2 bis 11 und 997:")
    for p in primes:
        display(fermat(p), p)

    print("\nErgebnisse für Nicht-Primzahlen:")
    for p in non_primes:
        display(fermat(p), p)
