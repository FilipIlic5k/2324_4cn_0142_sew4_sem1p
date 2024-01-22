"""
__author__ = "Filip Ilic"
__email__ = "filip.ilic@htl.rennweg.at"
__version__ = "1.0.0"
__copyright__ = "Copyright 2024"
__license__ = "GPL"
__status__ = "Development"
"""


from time import time


t0 = time()

def M(n, depth=0):
    """
    McCarthy's 91 function.

    The results of evaluating the function are given by M(n) = 91 for all integer arguments n ≤ 100, and M(n) = n − 10 for n > 100.
    Indeed, the result of M(101) is also 91 (101 - 10 = 91).
    All results of M(n) after n = 101 are continually increasing by 1, e.g. M(102) = 92, M(103) = 93.

    >>> m1 = M(87); m1
    (91, 11)

    >>> m2 = M(99); m2
    (91, 2)

    >>> m3 = M(101); m3
    (91, 0)

    >>> m4 = M(122); m4
    (112, 0)

    :param n: input number
    :return: result of the function
    """
    if n <= 100:
        return M(M(n + 11, depth + 1)[0], depth + 1)
    else:
        return n - 10, depth


m_list = [ M(n) for n in range(0, 200) ]
m_dict = {n: M(n) for n in range(0, 200)}

print(m_list)
print(m_dict)
print("Die Berechnung dauert", time() - t0, "Sekunden.")
# Find the tuple with the maximum recursion depth
max_tuple = max(m_dict, key=lambda n: m_dict[n][1])
print("Die Rekursionstiefe ist maximal bei n =", max_tuple, "und beträgt", m_dict[max_tuple][1])
