"""
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3
and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The
lexicographic permutations of 0, 1 and 2 are:

012, 021, 102, 120, 201, 210.

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""

import itertools

try:
    import lib
except ModuleNotFoundError:
    from questions import lib


ANSWER = 2783915460


# TODO come up with my own solution
def permutations(digits: list[int]) -> list[tuple[int, ...]]:
    """
    Find the lexicographic permutations of a list of integers.

    :param digits: a list of integers.

    :return: a list of permutations. Each permutation is a tuple with the integers in their order.
    """
    return list(itertools.permutations(digits))


@lib.profiling.profileit()
def find_permutation(digits: list[int], n: int) -> int:
    """
    Find the n-th lexicographic permutation of a given set of digits and convert it back to a single number.

    :param digits: a list of digits.
    :param n: which permutation to take.

    :return: an integer representation of a lexicographic permutation of digits.
    """
    # The permutation is a tuple of ints, so we convert them each into strings and join into one:
    result = "".join(map(str, permutations(digits)[n - 1]))

    # Convert back to an int:
    return int(result)


if __name__ == '__main__':

    answer = find_permutation(range(10), int(1e6))
