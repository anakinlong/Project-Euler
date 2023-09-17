"""
Things which are very general or don't fit into any of the existing groups.
"""

from . import primes


def euler_totient(n: int):
    """
    Evaluate the Euler totient function at n.

    https://en.wikipedia.org/wiki/Euler%27s_totient_function

    :param n: an integer

    :return: the Euler totient function at n.
    """
    # We start with n:
    product = n

    # Then for each prime factor p of n, we multiply our product by 1 - (1 / p):
    for i in set(primes.prime_factors(n)):
        product *= 1 - (1 / i)

    return int(product)


def sum_of_digits(n: int) -> int:
    """
    Calculate the sum of the digits of an integer.

    :param n: an integer.

    :return: the sum of its digits.
    """
    # Convert to a string and add each digit:
    digits = str(n)
    total = 0
    for digit in digits:
        total += int(digit)

    return total
