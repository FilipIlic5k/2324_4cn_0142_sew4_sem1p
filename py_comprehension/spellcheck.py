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
    210
    >>> len(edit1(''))
    30
    """
    try:
        letters = "abcdefghijklmnopqrstuvwxyzäöüß"
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


def edit1_good(word: str, all_words: Set[str]) -> Set[str]:
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
        all_words_lower = {w.lower() for w in all_words}
        possible_words = edit1(word.lower())
        valid_words = possible_words & all_words_lower
        final_words = {o for o in all_words if o.lower() in valid_words}
        return final_words
    except Exception as e:
        print(f"Error: {e}")
        return set()


def edit2_good(word: str, all_words: Set[str]) -> Set[str]:
    """
    Returns all words that are two edit away from the given word.
    :param word:
    :param all_words:
    :return:

    """
    try:
        word = word.lower()
        all_words_lower = {w.lower() for w in all_words}

        possible_two_edit = set()
        one_edit = edit1(word)
        for word in one_edit:
            possible_two_edit.update(edit1(word))

        valid_words = possible_two_edit & all_words_lower
        final_words = {o for o in all_words if o.lower() in valid_words}
        return final_words
    except Exception as e:
        print(f"Error: {e}")
        return set()


def correct(word: str, all_words: Set[str]) -> Set[str]:
    """
    Lists all possible corrections for the given word.
    It is eather in dictionary or one or two edits away from a word in the dictionary.
    :param word:
    :param all_words:
    :return:

    >>> words = read_all_words("de-en.txt")
    >>> correct("Aalsuppe", words)
    {'Aalsuppe'}

    >>> correct("Alsuppe", words)
    {'Aalsuppe'}

    >>> correct("Alsupe", words)
    {'Aalsuppe'}

    >>> sorted(correct("Alsupe", words))
    ['Aalsuppe', 'Absude', 'Lupe', 'alse']
    """
    try:
        word = word.lower()
        all_words_lower = {w.lower() for w in all_words}
        original_to_lower_mapping = {w.lower(): w for w in all_words}

        if word in original_to_lower_mapping:
            return {original_to_lower_mapping[word]}
        one_edit = edit1_good(word, all_words)
        if one_edit:
            return one_edit
        two_edit = edit2_good(word, all_words)
        if two_edit:
            return two_edit
        return {word}
    except Exception as e:
        print(f"Error: {e}")
        return set()