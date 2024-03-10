"""
__author__ = "Filip Ilic"
__email__ = "filip.ilic@htl.rennweg.at"
__version__ = "1.0.0"
__copyright__ = "Copyright 2024"
__license__ = "GPL"
__status__ = "Development"
"""
import string
from collections.abc import Set
from typing import List, Tuple


def read_all_words(filename: str) -> Set[str]:
    """
    Reads all words from the given file and returns them as a set.
    :param filename:
    :return: set of words

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
        print(f"Error: {e}")
        return set()


def split_word(word: str) -> List[Tuple[str, str]]:
    """
    Splits the given word into all possible combinations of two words.
    :param word:
    :return: list of tuples

    >>> split_word("abc")
    [('', 'abc'), ('a', 'bc'), ('ab', 'c'), ('abc', '')]

    >>> split_word("")
    [('', '')]

    >>> split_word("a")
    [('', 'a'), ('a', '')]
    """
    try:
        return [(word[:i], word[i:]) for i in range(len(word) + 1)]
    except Exception as e:
        print(f"Error: {e}")
        return []


def edit1(word: str) -> Set[str]:
    """
    Returns all words that are one edit away from the given word.
    :param word:
    :return:

    >>> len(edit1('abc'))
    182
    >>> len(edit1(''))
    26
    """
    try:
        letters = string.ascii_lowercase
        splits = split_word(word)
        deletes = [a + b[1:] for a, b in splits if b]  # removes one letter
        transposes = [a + b[1] + b[0] + b[2:] for a, b in splits if len(b) > 1]  # swaps two adjacent letters
        replaces = [a + c + b[1:] for a, b in splits for c in letters if b]  # replaces every letter with every letter
        # of the alphabet
        inserts = [a + c + b for a, b in splits for c in letters]  # inserts every letter of the alphabet between two
        # letters
        return set(deletes + transposes + replaces + inserts)
    except Exception as e:
        print(f"Error: {e}")
        return set()


def edit1_good(word: str, all_words: List[str]) -> Set[str]:
    """
    Returns all words that are one edit away from the given word.
    :param word:
    :param all_words:
    :return:

    >>> all_words = {'abc', 'acb', 'bac', 'bbc', 'a', 'ab', 'abcde'}
    >>> sorted(edit1_good('abc', all_words))
    ['ab', 'abc', 'acb', 'bac', 'bbc']

    """
    try:
        word = word.lower()
        possible_words = edit1(word)
        return possible_words & set(all_words)
    except Exception as e:
        print(f"Error: {e}")
        return set()
