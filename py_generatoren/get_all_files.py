"""
__author__ = "Filip Ilic"
__email__ = "filip.ilic@htl.rennweg.at"
__version__ = "1.0.0"
__copyright__ = "Copyright 2024"
__license__ = "GPL"
__status__ = "Development"
"""

import os
from collections.abc import Iterable, Generator
from typing import TextIO


def get_all_files(path: os.PathLike | str):
    """
    Generator function to yield all files in a given directory and its subdirectories.
    :param path: path to the directory
    :return: file in the directory

    >>> list(get_all_files("../py_oop/"))
    ['../py_oop/Fraction.py', '../py_oop/__pycache__/Fraction.cpython-312.pyc']
    """
    try:
        for entry in os.listdir(path):
            full_path = os.path.join(path, entry)
            if os.path.isdir(full_path):
                yield from get_all_files(full_path)
            else:
                yield full_path
    except PermissionError:
        print("Permission denied for " + path)
        pass
    except FileNotFoundError:
        print("File not found: " + path)
        pass
    except Exception as e:
        print("An error occurred: " + str(e))
        pass


def open_files(filenames: Iterable[str]) -> Generator[TextIO, None, None]:
    """
    Generator function to open files and yield file handles.

    :param filenames: Iterable of filenames
    :return: Generator yielding file handles
    """
    for fn in filenames:
        with open(fn) as f:
            yield f


def read_lines(files: Iterable[TextIO]) -> Generator[str, None, None]:
    """
    Generator function to read lines from file handles.

    :param files: Iterable of file handles
    :return: Generator yielding lines
    """
    for f in files:
        for line in f:
            yield line.rstrip()


def print_lines(lines: Iterable[str]) -> None:
    """
    Function to print lines, stripping trailing whitespace.

    :param lines: Iterable of lines
    """
    for line in lines:
        print(line)


if __name__ == "__main__":
    directory_path = "/home/filip-ilic/Dokumente/Developer/Oracle/Oracle_XE"
    for file in get_all_files(directory_path):
        print(file)

    fl = get_all_files(".")  # fl = "Liste" mit Filenamen
    of = open_files(fl)  # of = "Liste" mit offenen Files
    lines = read_lines(of)
    print_lines(lines)
