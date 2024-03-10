"""
__author__ = "Filip Ilic"
__email__ = "filip.ilic@htl.rennweg.at"
__version__ = "1.0.0"
__copyright__ = "Copyright 2024"
__license__ = "GPL"
__status__ = "Development"
"""
from collections.abc import Set


def read_all_words(filename: str) -> Set[str]:
    """
    Reads all words from the given file and returns them as a set.
    :param filename:
    :return:

    >>> wc = len(read_all_words("words.txt")); wc
    3

    >>> read_all_words("words2.txt")
    File not found.
    set()
    """
    try:
        with open(filename, "r") as file:
            return set(file.read().splitlines())
    except FileNotFoundError:
        print("File not found.")
        return set()
    except PermissionError:
        print("Permission denied.")
        return set()
    except Exception as e:
        print(e)
        return set()



