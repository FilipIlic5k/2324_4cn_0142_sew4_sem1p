"""
__author__ = "Filip Ilic"
__email__ = "filip.ilic@htl.rennweg.at"
__version__ = "1.0.0"
__copyright__ = "Copyright 2024"
__license__ = "GPL"
__status__ = "Development"
"""

import os


def get_all_files(path: str):
    """
    Generator function to yield all files in a given directory and its subdirectories.
    :param path: path to the directory
    :return: file in the directory

    >>> p = get_all_files("C:/")
    >>> next(p)
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


if __name__ == "__main__":
    directory_path = "/home/filip-ilic/"
    for file in get_all_files(directory_path):
        print(file)
