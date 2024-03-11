"""
__author__ = "Filip Ilic"
__email__ = "filip.ilic@htl.rennweg.at"
__version__ = "1.0.0"
__copyright__ = "Copyright 2024"
__license__ = "GPL"
__status__ = "Development"
"""
from collections import Counter
from typing import List, Set, Tuple

from py_Kasiski.Caesar.caesar import Caesar
from py_Kasiski.Vigenere.vigenere import Vigenere


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

    def dist_n_list(self, text: str, laenge: int) -> list[int]:
        """Wie dist_tuple, liefert aber nur eine aufsteigend sortierte Liste der
        Abstände ohne den Text zurück. In der Liste soll kein Element mehrfach vorkommen.
        Usage examples:
        >>> k = Kasiski()
        >>> k.dist_n_list("heissajucheieinei", 2)
        [2, 3, 5, 9, 11, 14]
        >>> k.dist_n_list("heissajucheieinei", 3)
        [9]
        >>> k.dist_n_list("heissajucheieinei", 4)
        []
        """
        dist = self.dist_n_tuple(text, laenge)
        return sorted(set([d for (_, d) in dist]))

    def ggt(self, x: int, y: int) -> int:
        """
        Ermittelt den größten gemeinsamen Teiler von x und y. Mit dem Euclidischen Algorithmus.
        Usage examples:
        >>> k = Kasiski()
        >>> k.ggt(10, 25)
        5
        >>> k.ggt(3, 6)
        3
        """
        while y:
            x, y = y, x % y
        return x

    def ggt_count(self, zahlen: List[int]) -> Counter:
        """
        Ermittelt den größten gemeinsamen Teiler von x und y.
        Usage examples:
        >>> k = Kasiski()
        >>> k.ggt(10, 25)
        5
        >>> k.ggt(10, 25)
        5
        >>> from collections import Counter
        >>> c=Counter([5,8,6,5,3,8,5,3,6,5])
        >>> print(c)
        Counter({5: 4, 8: 2, 6: 2, 3: 2})
        >>> c.most_common()
        [(5, 4), (8, 2), (6, 2), (3, 2)]
        """
        return Counter([self.ggt(zahlen[i], zahlen[i + 1]) for i in range(len(zahlen) - 1)])

    def get_nth_letter(self, s: str, start: int, n: int) -> str:
        """
        Extrahiert aus s jeden n. Buchstaben beginnend mit index start.
        Usage examples:
        >>> k = Kasiski()
        >>> k.get_nth_letter("Das ist kein kreativer Text.", 1, 4)
        'asektrx'
        """
        return ''.join([s[i] for i in range(start, len(s), n)])

    def crack_key(self, len: int) -> str:
        """
        Crackt den Key mit der Länge len
        :param len:
        :return:

        >>> string: str = 'In der faszinierenden Welt der Netzwerktechnik erstrecken sich endlose Möglichkeiten. Netzwerke sind essenziell für die Kommunikation zwischen Geräten, wobei Ethernet-Kabel, Switches und Router eine zentrale Rolle spielen. Sie ermöglichen ein reibungsloses Datenmanagement, wobei das Internetprotokoll (IP) als grundlegende Struktur dient. Ein effizientes Netzwerk erfordert sorgfältige Planung, um Engpässe zu vermeiden. Die ständige Evolution führt zu neuen Technologien wie 5G und Edge Computing. Die Sicherheit von Netzwerken ist ebenfalls von höchster Bedeutung, wobei Firewalls und Verschlüsselung eine entscheidende Schutzschicht bieten. Insgesamt ist die Netzwerktechnik ein vitaler Bestandteil unseres digitalen Zeitalters.'
        >>> vigenere = Vigenere()
        >>> crypt_str = vigenere.encrypt(string, "ilic")
        >>> kasiski = Kasiski(crypt_str)
        >>> kasiski.crack_key(4)
        'ilic'
        >>> crypt_str = vigenere.encrypt(string, "hugo")
        >>> kasiski = Kasiski(crypt_str)
        >>> kasiski.crack_key(4)
        'hugo'
        """
        try:
            substr_distances = self.dist_n_list(self.crypttext, len) # Abstände der Teilstrings

            factors_counter = self.ggt_count(substr_distances) # Counter mit den häufigsten Abständen

            key_length = factors_counter.most_common(1)[0][0] # häufigster Abstand

            potential_keys = [self.get_nth_letter(self.crypttext, i, key_length) for i in range(key_length)] # mögliche Schlüssel

            caesar = Caesar()
            return "".join([caesar.crack(key)[0] for key in potential_keys]) # Schlüssel cracken
        except Exception as e:
            print(f"Error: {e}")
            return ""

