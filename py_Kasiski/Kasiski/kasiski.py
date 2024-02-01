"""
__author__ = "Filip Ilic"
__email__ = "filip.ilic@htl.rennweg.at"
__version__ = "1.0.0"
__copyright__ = "Copyright 2024"
__license__ = "GPL"
__status__ = "Development"
"""
from typing import List, Set, Tuple


class Kasiski:
    def __init__(self, crypttext: str = ""):
        """
        Constructor. Initializes the crypttext.
        :param crypttext:
        """
        self.crypttext = crypttext

    def allpos(self, text: str, teilstring: str) -> List[int]:
        """
        Berechnet die Positionen von teilstring in text.
        Usage examples:
        >>> k = Kasiski()
        >>> k.allpos("heissajuchei, ein ei", "ei")
        [1, 10, 14, 18]
        >>> k.allpos("heissajuchei, ein ei", "hai")
        []
        """
        pos = []
        i = 0
        while i < len(text):
            if text[i:i + len(teilstring)] == teilstring:
                pos.append(i)
                i += len(teilstring)
            else:
                i += 1
        return pos

    def alldist(self, text: str, teilstring: str) -> Set[int]:
        """
        Berechnet die Abstände zwischen den Wiederholungen des Teilstrings im verschlüsselten Text.
        Usage examples:
        >>> k = Kasiski()
        >>> k.alldist("heissajuchei, ein ei", "ei")
        {4, 8, 9, 13, 17}
        >>> k.alldist("heissajuchei, ein ei", "hai")
        {}
        """
        pos = self.allpos(text, teilstring)
        dist = set()

        if not pos:
            return {}

        for i in range(len(pos)):
            for j in range(i + 1, len(pos)):
                dist.add(pos[j] - pos[i])
        return dist

    def dist_n_tuple(self, text: str, laenge: int) -> Set[Tuple[str, int]]:
        """
        Überprüft alle Teilstrings aus text mit der gegebenen laenge und liefert ein Set
        mit den Abständen aller Wiederholungen der Teilstrings in text.
        Usage examples:
        >>> k = Kasiski()
        >>> k.dist_n_tuple("heissajuchei", 2) == {('ei', 9), ('he', 9)}
        True
        >>> k.dist_n_tuple("heissajuchei", 3) == {('hei', 9)}
        True
        >>> k.dist_n_tuple("heissajuchei", 4) == set()
        True
        >>> k.dist_n_tuple("heissajucheieinei", 2) == \
        {('ei', 5), ('ei', 14), ('ei', 3), ('ei', 9), ('ei', 11), ('he', 9), ('ei', 2)}
        True
        """
        result = set()
        for i in range(len(text) - laenge + 1):
            substring = text[i:i + laenge]

            pos = self.allpos(text, substring)
            for j in range(len(pos)):
                for k in range(j + 1, len(pos)):
                    dist = pos[k] - pos[j]
                    result.add((substring, dist))
        return result

    def dist_n_list(self, text: str, laenge: int) -> List[int]:
        """
        Wie dist_tuple, liefert aber nur eine aufsteigend sortierte Liste der
        Abstände ohne den Text zurück. In der Liste soll kein Element mehrfach vorkommen.
        Usage examples:
        >>> k = Kasiski()
        >>> k.dist_n_list("heissajucheieinei", 2)
        [2, 3, 5, 9, 11, 14]
        >>> k.dist_n_list("heissajucheieinei", 3)
        [9]
        >>> k.dist_n_list("heissajucheieinei", 4)
        []
        """
        result = set()
        for i in range(len(text) - laenge + 1):
            substring = text[i:i + laenge]

            pos = self.allpos(text, substring)
            for j in range(len(pos)):
                for k in range(j + 1, len(pos)):
                    dist = pos[k] - pos[j]
                    result.add(dist)
        return sorted(list(result))
