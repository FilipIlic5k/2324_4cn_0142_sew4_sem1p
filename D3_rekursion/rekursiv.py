from time import time


t0 = time()

def M(n):
    """
    McCarthy's 91 function.

    The results of evaluating the function are given by M(n) = 91 for all integer arguments n ≤ 100, and M(n) = n − 10 for n > 100.
    Indeed, the result of M(101) is also 91 (101 - 10 = 91).
    All results of M(n) after n = 101 are continually increasing by 1, e.g. M(102) = 92, M(103) = 93.

    >>> m1 = M(87); m1
    91

    >>> m2 = M(99); m2
    91

    >>> m3 = M(101); m3
    91

    >>> m4 = M(122); m4
    112

    :param n: input number
    :return: result of the function
    """
    if n <= 100:
        return M(M(n + 11))
    else:
        return n - 10


m_list = [ M(n) for n in range(0, 200) ]
m_dict = [ (n, M(n)) for n in range(0, 200)]

#print(m_list)
#print(m_dict)
print("Die Berechnung dauert", time() - t0, "Sekunden.")
#print("Die Rekursionstiefe ist maximal bei n =", max(m_dict, key=m_dict.get), "und beträgt", m_dict[max(m_dict, key=m_dict.get)])
