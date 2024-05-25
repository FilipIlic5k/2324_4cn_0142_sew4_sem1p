"""
__author__ = "Filip Ilic"
__email__ = "filip.ilic@htl.rennweg.at"
__version__ = "1.0.0"
__copyright__ = "Copyright 2024"
__license__ = "GPL"
__status__ = "Development"
"""

import math
from typing import Callable, List, Any


def anwenden(fun: Callable[[Any], Any], liste: List[Any]) -> List[Any]:
    """
    Wendet die Funktion fun auf alle Elemente in der Liste an.

    :param fun: Eine Funktion, die auf jedes Element in der Liste angewendet wird.
    :param liste: Eine Liste von Elementen, auf die die Funktion angewendet wird.
    :return: Eine neue Liste mit den Ergebnissen der Funktionsanwendung auf die Elemente der ursprünglichen Liste.

    >>> anwenden(math.sin, [0, 1, 2, 3])
    [0.0, 0.8414709848078965, 0.9092974268256817, 0.1411200080598672]
    >>> anwenden(lambda x: x*x, [0, 1, 2, 3])
    [0, 1, 4, 9]
    """
    return [fun(x) for x in liste]


if __name__ == "__main__":
    print(anwenden(math.sin, [0, 1, 2, 3]))
    print(anwenden(lambda x: x * x, [0, 1, 2, 3]))
