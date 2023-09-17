"""
Things relating to Fibonacci numbers.
"""


from functools import lru_cache
import numpy as np


# Some useful constants - the golden ratio and its conjugate:
PHI = (1 + np.sqrt(5)) / 2
PSI = (1 - np.sqrt(5)) / 2


def nth_fibonacci(n: int) -> int:
    """
    Calculate the n-th term of the Fibonacci sequence using a very fast rounding method.
    WARNING: can be inaccurate for very large terms.

    https://en.wikipedia.org/wiki/Fibonacci_sequence#Computation_by_rounding

    :param n: which term from the sequence to calculate.

    :return: the n-th term of the Fibonacci sequence.
    """
    # TODO expand this to allow other values of PHI
    return round((PHI ** n) / np.sqrt(5))


def nth_fibonacci_looping(n: int, a_1: int, a_2: int) -> int:
    """
    Calculate the n-th term of the Fibonacci sequence using a looping method.
    This is generally the most reliable method I have currently.

    :param n: which term from the sequence to calculate.
    :param a_1: the first term of the sequence.
    :param a_2: the second term of the sequence.

    :return: the n-th term of the Fibonacci sequence.
    """
    # If it is the first or second term, we already know them:
    if n == 1:
        return a_1
    elif n == 2:
        return a_2
    # Otherwise, we will have to use these :
    else:
        previous_term = a_1
        current_term = a_2
        for _ in range(2, n):
            current_term, previous_term = current_term + previous_term, current_term

    return current_term


@lru_cache(maxsize=None)
def nth_fibonacci_recursive(n: int, a_1: int, a_2: int) -> int:
    """
    Calculate the n-th term of the Fibonacci sequence using a recursive method.
    This is basically just an excuse for me to use a cache.

    :param n: which term from the sequence to calculate.
    :param a_1: the first term of the sequence.
    :param a_2: the second term of the sequence.

    :return: the n-th term of the Fibonacci sequence.
    """
    # If it is the first or second term, we already know them:
    if n == 1:
        return a_1
    elif n == 2:
        return a_2
    # Otherwise, this term will be the sum of the previous two:
    else:
        return nth_fibonacci_recursive(n - 1, a_1, a_2) + nth_fibonacci_recursive(n - 2, a_1, a_2)


def next_fibonacci(a_1: int, a_2: int) -> int:
    """
    Calculate the next Fibonacci number in the sequence using the previous two.

    :param a_1: the (n - 2)-th value in the sequence.
    :param a_1: the (n - 1)-th value in the sequence.

    :return: the n-th value in the sequence.
    """
    return a_1 + a_2


def first_n_fibonacci(n: int, a_1: int, a_2: int) -> list[int]:
    """
    Return a list of the first n terms of the Fibonacci sequence.

    :param n: how many terms of the sequence to calculate.
    :param a_1: the first term of the sequence.
    :param a_2: the second term of the sequence.

    :return: the first n terms of the Fibonacci sequence.
    """
    # Create an empty list of the correct length:
    fibonacci_list = [0 for _ in range(n)]
    fibonacci_list[0] = a_1
    fibonacci_list[1] = a_2

    # Calculate subsequent terms and add to the list:
    previous_term = a_1
    current_term = a_2
    for i in range(2, n):
        current_term, previous_term = current_term + previous_term, current_term
        fibonacci_list[i] = current_term

    return fibonacci_list
