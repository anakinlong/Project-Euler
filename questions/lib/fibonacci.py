"""
Things relating to Fibonacci numbers.
"""


import numpy as np


# Some useful constants - the golden ratio and its conjugate:
PHI = (1 + np.sqrt(5)) / 2
PSI = (1 - np.sqrt(5)) / 2


def nth_fibonacci(n: int) -> int:
    """
    Calculate the n-th term of the Fibonacci sequence.

    https://en.wikipedia.org/wiki/Fibonacci_sequence#Computation_by_rounding

    :param n: which term from the sequence.

    :return: the n-th term of the Fibonacci sequence.
    """
    # TODO expand this to allow other values of PHI
    return round((PHI ** n) / np.sqrt(5))


def next_fibonacci(a_1: int, a_2: int) -> int:
    """
    Calculate the next Fibonacci number in the sequence using the previous two.

    :param a_1: the (n - 2)-th value in the sequence.
    :param a_1: the (n - 1)-th value in the sequence.

    :return: the n-th value in the sequence.
    """
    return a_1 + a_2
