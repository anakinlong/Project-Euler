"""
n! means n x (n - 1) x ... x 3 x 2 x 1.

For example, 10! = 10 x 9 x ... x 3 x 2 x 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!.
"""

import math

try:
    import lib
except ModuleNotFoundError:
    from questions import lib


ANSWER = 648


@lib.profiling.profileit()
def sum_of_factorial_digits(n: int) -> int:
    """
    Find the sum of the digits of n! (n factorial).

    :param n: an integer.

    :return: the sum of the digits of n!.
    """
    n_factorial = math.factorial(n)

    return lib.general.sum_of_digits(n_factorial)


if __name__ == '__main__':

    answer = sum_of_factorial_digits(100)
