"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6, and 9. The sum of these
multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

from typing import Iterable


ANSWER = 233168


def sum_of_multiples(factors: list[int], values: Iterable[int]) -> int:
    """
    Find the sum of all the integers in values which are multiples of any of the integers in factors.

    :param factors: a list of integers.
    :param values: a list of integers.

    :return: the sum of all the integers in values which are multiples of any of the integers in factors.
    """
    # Create a dictionary mapping each number in values to whether it is a multiple of any of the factors:
    value_to_is_multiple = {value: any([value % factor == 0 for factor in factors]) for value in values}

    # Sum the values which are multiples:
    return sum([value for value, is_multiple in value_to_is_multiple.items() if is_multiple])


if __name__ == "__main__":

    answer = sum_of_multiples([3, 5], range(1, 1000))
