class BritishLength:
    """
    Class for British length units.
    """

    def __init__(self, feet: int = 1, inches: int = 0):
        """
        Constructor for BritishLength.
        :param feet:
        :param inches:

        >>> one_foot = BritishLength(1); str(one_foot)
        '1 ft (0.3048 m)'
        >>> b1 = BritishLength(6); str(b1)
        '6 ft (1.8288 m)'
        >>> b2 = BritishLength(7, 3); str(b2)
        '7 ft, 3 in (2.2098 m)'
        >>> b3 = BritishLength(-14, 4); str(b3)
        '-13 ft, -8 in (-4.1656 m)'
        >>> b4 = BritishLength(3, 17); str(b4)
        '4 ft, 5 in (1.3462 m)'
        >>> b5 = BritishLength(4, -8); str(b5)
        '3 ft, 4 in (1.0160 m)'
        >>> b6 = BritishLength(-6, 5); str(b6)
        '-5 ft, -7 in (-1.7018 m)'
        >>> b7 = BritishLength(2, -28); str(b7)
        '-4 in (-0.1016 m)'
        """
        self._inches = convert_feet_to_inches(feet) + inches
        self._metric_length = convert_inches_to_cm(self.inches) / 100

    def __str__(self):
        """
        String representation of BritishLength.
        :return: str
        """
        try:
            # Calculate absolute values for display, determine the sign based on total inches
            abs_inches = abs(self._inches)
            feet, inches = divmod(abs_inches, 12)
            sign = "-" if self._inches < 0 else ""

            if inches == 0 and feet != 0:
                return f"{sign}{feet} ft ({self._metric_length:.4f} m)"
            elif feet == 0 and inches != 0:
                return f"{sign}{inches} in ({self._metric_length:.4f} m)"
            elif feet == 0 and inches == 0:
                return "0 ft (0.0000 m)"
            else:
                return f"{sign}{feet} ft, {sign}{inches} in ({self._metric_length:.4f} m)"
        except Exception as e:
            return f"Error: {e}"

    def __add__(self, other):
        """
        Add two BritishLength objects.
        :param other: BritishLength
        :return: BritishLength

        >>> print(BritishLength(7, 8) + BritishLength(3, 9));
        11 ft, 5 in (3.4798 m)
        >>> print((BritishLength(7, 8) + BritishLength(3, 9)) == BritishLength(11, 5))
        True
        >>> print(BritishLength(7, 8) + BritishLength(3, 4))
        11 ft (3.3528 m)
        >>> print((BritishLength(7, 8) + BritishLength(3, 4)) == BritishLength(11))
        True
        """
        try:
            total_inches = self.inches + other.inches
            feet, inches = divmod(total_inches, 12)
            return BritishLength(feet, inches)
        except Exception as e:
            return f"Error: {e}"

    def __sub__(self, other):
        """
        Subtract two BritishLength objects.
        :param other: BritishLength
        :return: BritishLength

        >>> print(BritishLength(7, 8) - BritishLength(3, 9))
        3 ft, 11 in (1.1938 m)
        >>> print((BritishLength(7, 8) - BritishLength(3, 9)) == BritishLength(3, 11))
        True
        >>> print(BritishLength(7, 8) - BritishLength(3, 4))
        4 ft, 4 in (1.3208 m)
        >>> print((BritishLength(7, 8) - BritishLength(3, 4)) == BritishLength(4, 4))
        True
        >>> print(BritishLength(7, 8) - BritishLength(11, 4))
        -4 ft, 4 in (-1.3208 m)
        >>> print((BritishLength(7, 8) - BritishLength(11, 4)) == BritishLength(-4, 4))
        True
        """
        try:
            total_inches = self.inches - other.inches
            print(total_inches)
            feet, inches = divmod(total_inches, 12)
            return BritishLength(feet, inches)
        except Exception as e:
            return f"Error: {e}"

    def __mul__(self, other):
        """
        Multiply two BritishLength objects.
        :param other:
        :return:
        >>> print(BritishLength(3, 7) * 4)
        14 ft, 4 in (4.3688 m)
        >>> print(BritishLength(3, 7) * 0)
        0 ft (0.0000 m)
        >>> print(BritishLength(3, 7) * -4)
        -13 ft, -8 in (-4.1656 m)
        >>> print(BritishLength(3, 7) * -1)
        -3 ft, 7 in (-1.0922 m)
        """
        try:
            if not isinstance(other, int):
                return NotImplemented
            total_inches = self.inches * other
            if total_inches < 0:
                feet, inches = divmod(abs(total_inches), 12)
                return BritishLength(-feet, inches)
            else:
                feet, inches = divmod(total_inches, 12)
                return BritishLength(feet, inches)
        except Exception as e:
            return f"Error: {e}"

    def __eq__(self, other):
        """
        Compare two BritishLength objects.
        :param other: BritishLength
        :return: bool

        >>> BritishLength(7, 8) == BritishLength(7, 8)
        True
        >>> BritishLength(7, 8) == BritishLength(7, 9)
        False
        """
        return self.inches == other.inches

    @property
    def feet(self):
        return self._inches // 12

    @property
    def inches(self):
        return self._inches

    @property
    def metric_length(self):
        return self._metric_length


def convert_feet_to_inches(feet: int) -> int:
    return feet * 12


def convert_inches_to_cm(inches: int) -> float:
    return inches * 2.54


def fibo():
    """
    Generator for an infinite list of Fibonacci BritishLength numbers.
    Starts with 1 inch, 1 inch, and each subsequent value is the sum of the two previous values.
    """
    # Initialize the first two BritishLength objects
    a = BritishLength(0, 1)  # Equivalent to 1 inch
    b = BritishLength(0, 1)  # Equivalent to 1 inch
    while True:
        yield a
        next_value = a + b  # Calculate the sum of the two previous values
        a = b  # Move forward: a becomes b
        b = next_value  # Move forward: b becomes the sum of the previous two values

def primes():
    """
    Generator for an infinite list of prime numbers.
    """
    # Initialize the first prime number
    prime = 2
    while True:
        yield prime
        # Find the next prime number
        while True:
            prime += 1
            for i in range(2, prime):
                if prime % i == 0:
                    break
            else:
                break

if __name__ == "__main__":
    # Example of using the generator
    generator = fibo()
    for _ in range(10):  # Print the first 10 Fibonacci BritishLength numbers
        fib_number = next(generator)
        print(str(fib_number))

    generator2 = primes()
    for _ in range(10):  # Print the first 10 prime numbers
        prime_number = next(generator2)
        print(prime_number)
