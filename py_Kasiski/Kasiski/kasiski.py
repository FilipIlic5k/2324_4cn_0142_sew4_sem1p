"""
__author__ = "Filip Ilic"
__email__ = "filip.ilic@htl.rennweg.at"
__version__ = "1.0.0"
__copyright__ = "Copyright 2024"
__license__ = "GPL"
__status__ = "Development"
"""
from typing import List


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
