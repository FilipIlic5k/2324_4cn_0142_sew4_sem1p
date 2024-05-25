"""
__author__ = "Filip Ilic"
__email__ = "filip.ilic@htl.rennweg.at"
__version__ = "1.0.0"
__copyright__ = "Copyright 2024"
__license__ = "GPL"
__status__ = "Development"
"""

import functools
import traceback

def debug(func):
    """
    Dekorator, der die Parameter und das Ergebnis einer Funktion ausgibt.

    :param func: Die zu dekorierende Funktion
    :return: Die dekorierte Funktion
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        indent = "  " * wrapper.call_count
        print(f"{indent}Calling {func.__name__} with args={args}, kwargs={kwargs}")
        try:
            result = func(*args, **kwargs)
            print(f"{indent}{func.__name__} returned {result}")
        except Exception as e:
            print(f"{indent}{func.__name__} raised an exception: {e}")
            raise
        finally:
            wrapper.call_count -= 1
        return result

    wrapper.call_count = 0
    return wrapper

@debug
def example_function(x, y):
    """Eine Beispiel-Funktion, die zwei Zahlen addiert."""
    return x + y

@debug
def factorial(n):
    """Rekursive Funktion zur Berechnung der Fakultät."""
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    # Beispielaufrufe
    print(example_function(3, 5))
    print(factorial(5))
