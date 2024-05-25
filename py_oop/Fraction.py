"""
__author__ = "Filip Ilic"
__email__ = "filip.ilic@htl.rennweg.at"
__version__ = "1.0.0"
__copyright__ = "Copyright 2024"
__license__ = "GPL"
__status__ = "Development"
"""


class Fraction:
    """
    Represents a fraction.
    >>> f = 1 + Fraction(1, 2); str(f)
    '1 1/2'
    >>> str(1 + Fraction(1, 2))
    '1 1/2'
    >>> str(Fraction(1, 2) + 1)
    '1 1/2'
    >>> str(2 - Fraction(1, 2))
    '1 1/2'
    >>> str(Fraction(1, 3) - 2)
    '-1 2/3'
    >>> str(3 * Fraction(1, 2))
    '1 1/2'
    >>> str(Fraction(1, 2) * 3)
    '1 1/2'
    >>> str(4 / Fraction(2, 3))
    '6'
    >>> str(Fraction(1, 2) / 2)
    '1/4'
    """
    def __init__(self, numerator: int = 0, denominator: int = 1):
        """
        Constructor.
        :param numerator:
        :param denominator:
        >>> f = Fraction(6, 9)
        >>> str(f)
        '2/3'
        >>> f = Fraction(20, -4)
        >>> str(f)
        '-5'
        >>> Fraction(1, 0)  # This should raise an error
        Traceback (most recent call last):
           ...
        ValueError: Nenner darf nicht 0 sein.
        """
        if denominator == 0:
            raise ValueError("Nenner darf nicht 0 sein.")
        self._numerator = numerator
        self._denominator = denominator
        self._reduce()

    def __str__(self):
        """
        Returns the fraction as a string.
        :return: fraction as a string

        >>> f = Fraction(8, 12); str(f)
        '2/3'
        >>> f = Fraction(5, 3); str(f)
        '1 2/3'
        >>> f = Fraction(-5, 3); str(f)
        '-1 2/3'
        >>> f = Fraction(1000, -150); str(f)
        '-6 2/3'
        """
        try:
            if self._denominator == 0:
                raise ValueError("Nenner darf nicht 0 sein.")

            ganze_zahl = abs(self._numerator) // self._denominator
            rest = abs(self._numerator) % self._denominator

            if abs(self._numerator) >= self._denominator:
                vorzeichen = "-" if self._numerator < 0 else ""
                if rest != 0:
                    if self._denominator == 1:
                        return f"{vorzeichen}{ganze_zahl}"
                    else:
                        return f"{vorzeichen}{abs(ganze_zahl)} {rest}/{self._denominator}"
                else:
                    return vorzeichen + str(ganze_zahl)
            else:
                return f"{self._numerator}/{self._denominator}"
        except Exception as e:
            print(f"Error: {e}")

    def __repr__(self):
        """
        Returns the fraction as a string.
        :return: fraction as a string

        >>> f = Fraction(8, 12); repr(f)
        'Fraction(2, 3)'
        """
        return f"Fraction({self._numerator}, {self._denominator})"

    def __add__(self, other):
        """
        Adds two fractions.
        :param other:
        :return: sum of two fractions

        >>> f1 = Fraction(1, 2); f2 = Fraction(1, 3); f1 + f2
        Fraction(5, 6)
        >>> f1 = Fraction(1, 2); f2 = Fraction(1, 4); f1 + f2
        Fraction(3, 4)
        >>> f1 = Fraction(1, 2); f2 = Fraction(4, 2); f1 + f2
        Fraction(5, 2)
        >>> str(f1+f2)
        '2 1/2'
        >>> str(Fraction(1, 2) + Fraction(2, 3))
        '1 1/6'
        >>> str(Fraction(-1, 2) + Fraction(1, 2))
        '0/1'
        """
        try:
            if isinstance(other, Fraction):
                new_numerator = self._numerator * other._denominator + other._numerator * self._denominator
                new_denominator = self._denominator * other._denominator
                self._reduce()
                return Fraction(new_numerator, new_denominator)
            elif isinstance(other, int):
                return self + Fraction(other)
            return NotImplemented
        except Exception as e:
            print(f"Error: {e}")
            return NotImplemented

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        """
        Subtracts two fractions.
        :param other:
        :return:
        >>> f1 = Fraction(1, 2); f2 = Fraction(1, 3); f1 - f2
        Fraction(1, 6)
        >>> f1 = Fraction(1, 2); f2 = Fraction(1, 4); f1 - f2
        Fraction(1, 4)
        >>> f1 = Fraction(1, 2); f2 = Fraction(4, 2); f1 - f2
        Fraction(-3, 2)
        >>> str(f1-f2)
        '-1 1/2'
        >>> str(Fraction(3, 4) - Fraction(1, 4))
        '1/2'
        >>> str(Fraction(-1, 2) - Fraction(-1, 2))
        '0/1'
        >>> str(Fraction(1, 8) - Fraction(1, 2))
        '-3/8'
        """
        try:
            if isinstance(other, Fraction):
                new_numerator = self._numerator * other._denominator - other._numerator * self._denominator
                new_denominator = self._denominator * other._denominator
                result = Fraction(new_numerator, new_denominator)
                result._reduce()
                return result
            elif isinstance(other, int):
                return self - Fraction(other)
            return NotImplemented
        except Exception as e:
            print(f"Error: {e}")
            return NotImplemented

    def __rsub__(self, other):
        if isinstance(other, int):
            return Fraction(other) - self
        return NotImplemented

    def __mul__(self, other):
        """
        Multiplies two fractions.
        :param other:
        :return:
        >>> f1 = Fraction(1, 2); f2 = Fraction(1, 3); f1 * f2
        Fraction(1, 6)
        >>> f1 = Fraction(1, 2); f2 = Fraction(1, 4); f1 * f2
        Fraction(1, 8)
        >>> f1 = Fraction(1, 2); f2 = Fraction(4, 2); f1 * f2
        Fraction(1, 1)
        >>> str(Fraction(3, 4) * Fraction(4, 3))
        '1'
        >>> str(Fraction(-2, 3) * Fraction(3, 4))
        '-1/2'
        >>> str(Fraction(0, 1) * Fraction(10, 5))
        '0/1'
        """
        try:
            if isinstance(other, Fraction):
                new_numerator = self._numerator * other._numerator
                new_denominator = self._denominator * other._denominator
                result = Fraction(new_numerator, new_denominator)
                result._reduce()
                return result
            elif isinstance(other, int):
                return self * Fraction(other)
            return NotImplemented
        except Exception as e:
            print(f"Error: {e}")
            return NotImplemented

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        """
        Divides two fractions. i. e. / operator.
        :param other:
        :return:
        >>> f1 = Fraction(1, 2); f2 = Fraction(1, 3); f1 / f2
        Fraction(3, 2)
        >>> f1 = Fraction(1, 2); f2 = Fraction(1, 4); f1 / f2
        Fraction(2, 1)
        >>> f1 = Fraction(1, 2); f2 = Fraction(4, 2); f1 / f2
        Fraction(1, 4)
        >>> str(Fraction(1, 2) / Fraction(1, 4))
        '2'
        >>> str(Fraction(-1, 3) / Fraction(1, 3))
        '-1'
        >>> str(Fraction(1, 2) / Fraction(-1, 2))
        '-1'
        >>> str(Fraction(-1, -2) / Fraction(1, 2))
        '1'
        >>> float(Fraction(5, 10) / Fraction(2, 5))
        1.25
        """
        try:
            if isinstance(other, Fraction):
                if other._numerator == 0:
                    raise ValueError("Division by zero.")
                new_numerator = self._numerator * other._denominator
                new_denominator = self._denominator * other._numerator
                if new_denominator == 0:
                    raise ValueError("Division by zero.")
                result = Fraction(new_numerator, new_denominator)
                result._reduce()
                return result
            elif isinstance(other, int):
                return self / Fraction(other)
            return NotImplemented
        except ValueError as e:
            print(f"Error: {e}")
            return NotImplemented
        except Exception as e:
            print(f"Error: {e}")
            return NotImplemented

    def __rtruediv__(self, other):
        if isinstance(other, int):
            return Fraction(other) / self
        return NotImplemented

    def __floordiv__(self, other):
        """
        Divides two fractions. Only the integer part is returned. i. e. // operator.
        :param other:
        :return:
        >>> f1 = Fraction(1, 2); f2 = Fraction(1, 3); f1 // f2
        Fraction(1, 1)
        >>> f1 = Fraction(1, 2); f2 = Fraction(1, 4); f1 // f2
        Fraction(2, 1)
        >>> f1 = Fraction(1, 2); f2 = Fraction(4, 2); f1 // f2
        Fraction(0, 1)
        """
        try:
            result = self.__truediv__(other)
            if result is not NotImplemented:
                return Fraction(result._numerator // result._denominator)
            return NotImplemented
        except Exception as e:
            print(f"Error: {e}")
            return NotImplemented

    def __eq__(self, other):
        """
        Compares two fractions.
        :param other:
        :return:
        >>> f1 = Fraction(1, 2); f2 = Fraction(1, 3); f1 == f2
        False
        >>> f1 = Fraction(1, 2); f2 = Fraction(1, 2); f1 == f2
        True
        """
        try:
            if isinstance(other, Fraction):
                return self._numerator == other._numerator and self._denominator == other._denominator
            return NotImplemented
        except Exception as e:
            print(f"Error: {e}")
            return NotImplemented

    def __float__(self):
        """
        Returns the fraction as a float. i. e. float(fraction)
        :return:
        >>> float(Fraction(1, 2))
        0.5
        >>> float(Fraction(1, 3))
        0.3333333333333333
        """
        return self._numerator / self._denominator
    def _reduce(self):
        """
        Reduces the fraction. example:  8/12 -> 2/3
        :return: None

        >>> f = Fraction(8, 12)
        >>> f._numerator
        2
        >>> f._denominator
        3
        """
        try:
            gcd = self._gcd(abs(self._numerator), self._denominator)
            self._numerator //= gcd
            self._denominator //= gcd
        except Exception as e:
            print(f"Error: {e}")

    def _gcd(self, a, b):
        """
        Calculates the greatest common divisor of a and b.
        :param a:
        :param b:
        :return: greatest common divisor

        >>> Fraction._gcd(None, 8, 12)
        4
        >>> Fraction._gcd(None, 17, 5)
        1
        >>> Fraction._gcd(None, 14, 21)
        7
        """
        try:
            while b:
                a, b = b, a % b
            return a
        except Exception as e:
            print(f"Error: {e}")

    @property
    def numerator(self):
        return self._numerator

    @property
    def denominator(self):
        return self._denominator

    @numerator.setter
    def numerator(self, value):
        self._numerator = value
        self._reduce()

    @denominator.setter
    def denominator(self, value):
        if value == 0:
            raise ValueError("Nenner darf nicht 0 sein.")
        self._denominator = value
        self._reduce()