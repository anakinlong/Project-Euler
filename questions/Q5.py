"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

import math

try:
    import lib
except ModuleNotFoundError:
    from questions import lib


ANSWER = 232792560


def prime_exponents(n: int) -> dict[int, int]:
    """
    Return a dictionary mapping the prime factors of n to their exponents.

    :param n: an integer.

    :return: a dictionary with the format {prime: exponent} for all of the prime factors of n.
    """
    prime_factors = lib.primes.prime_factors(n)

    return {prime: prime_factors.count(prime) for prime in prime_factors}


@lib.profiling.profileit()
def lowest_common_multiple(numbers: list[int]) -> int:
    """
    Find the lowest common multiple of a list of integers.

    :param numbers: a list of integers.

    :return: the lowest common multiple.
    """
    # Create a dictionary of each prime to the list of exponents from each n in numbers:
    all_prime_exponents = {n: prime_exponents(n) for n in numbers}
    # The set of all prime numbers in the prime factors of the given numbers:
    all_primes = {prime for prime_exponents in all_prime_exponents.values() for prime in prime_exponents}

    # A dictionary mapping each prime to a list of its exponents from each number:
    prime_to_exponents = {prime: [all_prime_exponents[n].get(prime, 0) for n in numbers] for prime in all_primes}
    # A dictionary mapping each prime to its maximum exponent from the dictionary above:
    prime_to_max_exponent = {prime: max(exponents) for prime, exponents in prime_to_exponents.items()}

    return math.prod([prime ** max_exponent for prime, max_exponent in prime_to_max_exponent.items()])


if __name__ == '__main__':

    lowest_common_multiple(range(1, 21))
