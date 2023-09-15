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
    for i in primes.prime_factors(n):
        product *= 1 - (1 / i)

    return product
