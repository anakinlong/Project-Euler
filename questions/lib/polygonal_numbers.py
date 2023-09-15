"""
Things relating to polygonal numbers, e.g. triangle, square, ... numbers.
"""

from typing import Callable


def triangle_number(n: int) -> int:
    """
    Generate the n-th triangle number.

    :param n: a positive integer.

    :return: the n-th triangle number.
    """
    return n * (n + 1) / 2


def square_number(n: int) -> int:
    """
    Generate the n-th square number.

    :param n: a positive integer.

    :return: the n-th square number.
    """
    return n ** 2


def pentagonal_number(n: int) -> int:
    """
    Generate the n-th pentagonal number.

    :param n: a positive integer.

    :return: the n-th pentagonal number.
    """
    return n * (3 * n - 1) / 2


def hexagonal_number(n: int) -> int:
    """
    Generate the n-th hexagonal number.

    :param n: a positive integer.

    :return: the n-th hexagonal number.
    """
    return n * (2 * n - 1)


def first_n_polygonal_numbers(polygonal_number: Callable[[int], int]) -> Callable[[int], list[int]]:
    """
    Return a function which returns the first n polygonal numbers, given the formula to calculate each one.

    :param polygonal_number: the function for calculating the n-th polygonal number.

    :return: a function which returns a list of the first n polygonal numbers.
    """

    def func(n: int) -> list[int]:

        return [polygonal_number(k) for k in range(1, n + 1)]

    return func


first_n_triangle_numbers = first_n_polygonal_numbers(triangle_number)
first_n_square_numbers = first_n_polygonal_numbers(square_number)
first_n_pentagonal_numbers = first_n_polygonal_numbers(pentagonal_number)
first_n_hexagonal_numbers = first_n_polygonal_numbers(hexagonal_number)
