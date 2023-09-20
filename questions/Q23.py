"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the
sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum
exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two
abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as
the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is
known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""

try:
    import lib
except ModuleNotFoundError:
    from questions import lib


ANSWER = 4179871


def abundant(n: int) -> bool:
    """
    Check whether n is an abundant number or not.

    :param n: an integer.

    :return: True if n is abundant, otherwise False.
    """
    return lib.factors.sum_of_proper_divisors(n) > n


def abundant_numbers(max_excl: int) -> list[int]:
    """
    Return a list of all the abundant numbers below a specified value.

    :param max_excl: the maximum (exclusive) value of each number.

    :return: a list of all the abundant numbers below max_excl.
    """
    # Starting with an empty list, check whether each number is abundant and add it if it is:
    all_abundant_numbers = []
    for n in range(1, max_excl):
        if abundant(n):
            all_abundant_numbers.append(n)

    return all_abundant_numbers


def find_numbers_not_sum_of_two_abundants(max_incl: int) -> list[int]:
    """
    Find all the positive integers below a specified value which cannot be written as the sum of two abundant numbers.

    :param max_incl: the maximum (inclusive) value of each number.

    :return: a list of integers.
    """
    # Get the list of abundant numbers:
    abundants = abundant_numbers(max_incl + 1)
    # A dictionary mapping each number to whether it can be written as the sum of two abundant numbers.
    # Start each number as False:
    numbers = {k: False for k in range(1, max_incl + 1)}
    n_abundants = len(abundants)
    for i in range(n_abundants):
        for j in range(n_abundants - i):
            abundant_1 = abundants[i]
            abundant_2 = abundants[j]
            if abundant_1 + abundant_2 <= max_incl:
                numbers[abundant_1 + abundant_2] = True

    return [number for number, written_as_sum in numbers.items() if not written_as_sum]


@lib.profiling.profileit()
def sum_numbers_not_sum_of_two_abundants() -> int:
    """
    Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

    :return: the total sum.
    """
    return sum(find_numbers_not_sum_of_two_abundants(28123))


if __name__ == '__main__':

    answer = sum_numbers_not_sum_of_two_abundants()
