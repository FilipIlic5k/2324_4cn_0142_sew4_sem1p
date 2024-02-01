"""
__author__ = "Filip Ilic"
__email__ = "filip.ilic@htl.rennweg.at"
__version__ = "1.0.0"
__copyright__ = "Copyright 2024"
__license__ = "GPL"
__status__ = "Development"
"""
from typing import List, Set


class Kasiski:
    def __init__(self, crypttext:str=""):
        """
        Constructor. Initializes the crypttext.
        :param crypttext:
        """
        self.crypttext = crypttext


    def allpos(self, text:str, teilstring:str) -> List[int]:
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
            if text[i:i+len(teilstring)] == teilstring:
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
            for j in range(i+1, len(pos)):
                dist.add(pos[j]-pos[i])
        return dist

