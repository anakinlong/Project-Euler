"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: As 1! = 1 and 2! = 2 are not sums they are not included.
"""

import math

try:
    import lib
except ModuleNotFoundError:
    from questions import lib


ANSWER = 40730


EXPLANATION = """
Since 9!x7 < 9999999, the numbers have at most 7 digits. So we can set an upper bound of 1e7.
"""

# Pre-calculate the factorials of the numbers 0-9:
FACTORIAL = {n: math.factorial(n) for n in range(0, 10)}


def digit_factorial_sum(n: int) -> int:
    """
    Calculate the sum of the factorial of each of the digits of an integer.

    :param n: an integer.

    :return: the sum of the factorial of each digit of n.
    """
    digits = str(n)
    total = 0
    for digit in digits:
        total += FACTORIAL[int(digit)]

    return total


# TODO could refine this seach a bit, since we currently search all numbers
@lib.profiling.profileit()
def curiousCheck(min_incl: int, max_excl: int) -> int:
    """
    Calculate the sum of all numbers for which the sum of the factorial of each of their digits equals themselves.

    :param min_incl: the minumum (inclusive) search value of the numbers.
    :param max_excl: the maximum (exclusive) seach value of the numbers.

    :return: the sum of all the numbers which have this property.
    """
    total = 0
    for n in range(min_incl, max_excl):
        if digit_factorial_sum(n) == n:
            total += n

    return total


if __name__ == '__main__':

    answer = curiousCheck(3, int(1e7))
