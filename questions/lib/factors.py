"""
Things relating to factors of integers.
"""

from typing import Callable

from . import generic_python


def factors(n: int) -> list[int]:
    """
    Return a list of all the proper factors of n (including 1 but not itself).

    :param n: an integer.

    :return: the proper factors of n.
    """
    # TODO use something better than lists, since you don't know how long the list will be
    # Every number has a proper factor of 1:
    all_factors = [1]

    # Now we loop through every integer between 1 and the square root of n to prevent repeats:
    for k in range(2, int(n ** (1 / 2) + 1)):
        # If n is divisible by k, add k to the list of proper factors:
        if n % k == 0:
            all_factors.append(int(k))

            # If n / k isn't k, i.e. k isn't the square root of n, also add n / k to the list of factors:
            if int(k) != int(n / k):
                all_factors.append(int(n / k))

    # Sort the list from smallest to largest:
    all_factors.sort()

    return all_factors


def count_factors(n: int) -> int:
    """
    Count how many proper factors n has (including 1 but not itself).

    :param n: an integer.

    :return: the number of proper factors of n.
    """
    # Every number has a proper factors of 1:
    n_factors = 1

    # Now we loop through every integer between 1 and the square root of n to prevent repeats:
    for k in range(2, int(n ** (1 / 2) + 1)):
        # If n is divisible by k, add k to the list of proper factors:
        if n % k == 0:
            n_factors += 1

            # If n / k isn't k, i.e. k isn't the square root of n, also add n / k to the list of factors:
            if int(k) != int(n / k):
                n_factors += 1

    return n_factors


def sum_of_proper_divisors(n: int) -> list[int]:
    """
    Return the sum of all the proper divisors of n (including 1 but not itself).

    :param n: an integer.

    :return: the sum of the proper factors of n.
    """
    # Every number has proper divisor of 1:
    total = 1

    # Now we loop through every integer between 1 and the square root of n to prevent repeats:
    for k in range(2, int(n ** (1 / 2) + 1)):
        # If n is divisible by k, add k to the total:
        if n % k == 0:
            total += int(k)

            # If n / k isn't k, i.e. k isn't the square root of n, also add n / k to the total:
            if int(k) != int(n / k):
                total += int(n / k)

    return total


def amicable(n: int) -> bool:
    """
    Check whether n is an amicable number or not.

    :param n: an integer.

    :return: True if n is amicable, otherwise False.
    """
    divisor_sum_n = sum_of_proper_divisors(n)

    return divisor_sum_n != n and sum_of_proper_divisors(divisor_sum_n) == n


def abundant(n: int) -> bool:
    """
    Check whether n is an abundant number or not.

    :param n: an integer.

    :return: True if n is abundant, otherwise False.
    """
    return sum_of_proper_divisors(n) > n


def deficient(n: int) -> bool:
    """
    Check whether n is a deficient number or not.

    :param n: an integer.

    :return: True if n is deficient, otherwise False.
    """
    return sum_of_proper_divisors(n) < n


def perfect(n: int) -> bool:
    """
    Check whether n is a perfect number or not.

    :param n: an integer.

    :return: True if n is perfect, otherwise False.
    """
    return sum_of_proper_divisors(n) == n


find_numbers_docstring = generic_python.docstrings.generate_docstring_decorator(
    """
    Return a list of all the {_name} numbers below a specified value.

    :param max_excl: the maximum (exclusive) value of each number.

    :return: a list of all the {_name} numbers below max_excl.
    """
)


def find_numbers(condition: Callable[[int], bool], name: str) -> list[int]:
    """
    Return a list of all the numbers below a specified value which meet a certain condition.

    :param condition: the function which decides whether each number meets the required conditions.
    :param name: the name of the type of number we are finding, e.g. "amicable".

    :return: a list of all the numbers below max_excl which meet a certain condition.
    """
    @find_numbers_docstring(_name=name)
    def func(max_excl: int) -> list[int]:
        # Starting with an empty list, check whether each number meets the condition and add it if it is:
        all_numbers = []
        for n in range(1, max_excl):
            if condition(n):
                all_numbers.append(n)

        return all_numbers

    return func


amicable_numbers = find_numbers(amicable, "amicable")
abundant_numbers = find_numbers(abundant, "abundant")
deficient_numbers = find_numbers(deficient, "deficient")
perfect_numbers = find_numbers(perfect, "perfect")
