"""
__author__ = "Filip Ilic"
__email__ = "filip.ilic@htl.rennweg.at"
__version__ = "1.0.0"
__copyright__ = "Copyright 2024"
__license__ = "GPL"
__status__ = "Development"
"""

import operator


def print_table(fun, title=""):
    """
    Druckt die Wahrheitstabelle der Funktion fun mit zwei boolean Operanden.

    :param fun: Die zu testende logische Funktion, die zwei boolean Werte als Argumente akzeptiert.
    :param title: Optionaler Titel für die Tabelle.
    """
    print(f"{title}")
    print("A     B     | Result")
    for a in [False, True]:
        for b in [False, True]:
            print(f"{a:<5} {b:<5} | {fun(a, b)}")


# Beispielaufrufe
if __name__ == "__main__":
    import doctest

    doctest.testmod()

    # Testaufrufe der print_table Funktion
    print_table(operator.or_, "OR")
    print_table(operator.and_, "AND")
    print_table(operator.xor, "XOR")
