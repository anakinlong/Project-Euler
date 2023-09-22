"""
Things relating to prime numbers.
"""

import math


def is_prime(n: int) -> bool:
    """
    Checks if an integer is prime.

    :param n: an integer.

    :return: True if n is prime, otherwise False.
    """
    # Check whether n is positive:
    if n <= 1:
        return False
    # Check whether n is 2:
    if n == 2:
        return True
    # Check whether n is even (but not 2):
    elif n % 2 == 0:
        return False
    # Check whether n is divisible by any odd numbers less than its square root:
    else:
        for k in range(3, int(n ** (1/2)) + 1, 2):
            if n % k == 0:
                return False
        return True


def prime_sieve(n: int) -> list[int]:
    """
    Returns a list of all primes less than or equal to n (inclusive).

    :param n: an integer.

    :return: a list of all the prime numbers less than or equal to n.
    """
    # We use a dictionary mapping all numbers to a bool of whether they are prime, since appending to a list would be
    # slow. This way we can have a dictionary of known size, decide whether each number is prime, and then create a list
    # of just the prime numbers afterwards.
    # Start off by setting all the numbers to True:
    primes = {k: True for k in range(2, n + 1)}

    # Now we loop through each prime, starting from the smallest, and set all their multiples to False:
    for k in primes:
        # We only want to do all this stuff for prime numbers, since that is sufficient to cover all multiples.
        # There is also no point doing this for any number larger than n / 2, since there won't be any multiples
        # smaller than n:
        if primes[k] and (k <= n / 2):
            multiples = range(2 * k, n + 1, k)
            # Set all the multiples to be not prime:
            for f in multiples:
                primes[f] = False

    # Return a list of all the numbers which are still mapped to True:
    return [k for k, is_prime in primes.items() if is_prime]


def prime_factors(n: int) -> list[int]:
    """
    Returns a list of all the prime factors of n (with repeats).

    :param n: an integer.

    :return: a list of prime factors ordered from smallest to largest with repeats.
    """
    # TODO use something better than lists, since you don't know how long the list will be
    # Start with an empty list of prime factors
    factors = []
    k = 2

    # Loop through all the numbers smaller than or equal to the square root of n:
    while k <= n ** (1 / 2):
        # If n is not divisible by k (i.e. has a remainder), increment k:
        if n % k:
            k += 1
        # If n is divisible by k, divide n by k and add k to the list.
        # Don't increment k in case n / k is also divisible by k:
        else:
            n /= k
            # Make sure n is an integer in case of floating point inaccuracy:
            n = round(n)
            factors.append(k)

    # If n is still greater than 1 it must be prime, so add to the list:
    if n > 1:
        factors.append(n)

    return factors


def prime_exponents(n: int) -> dict[int, int]:
    """
    Return a dictionary mapping the prime factors of n to their exponents.

    :param n: an integer.

    :return: a dictionary with the format {prime: exponent} for all of the prime factors of n.
    """
    factors = prime_factors(n)

    return {prime: factors.count(prime) for prime in factors}


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

    # A dictionary mapping each prime to its minimum exponent from all of the numbers:
    prime_to_max_exponent = {
        prime: max([all_prime_exponents[n].get(prime, 0) for n in numbers]) for prime in all_primes
    }

    return math.prod([prime ** max_exponent for prime, max_exponent in prime_to_max_exponent.items()])


def greatest_common_factor(numbers: list[int]) -> int:
    """
    Find the greatest common factor of a list of integers.

    :param numbers: a list of integers.

    :return: the greatest common factor.
    """
    # Create a dictionary of each prime to the list of exponents from each n in numbers:
    all_prime_exponents = {n: prime_exponents(n) for n in numbers}
    # The set of all prime numbers in the prime factors of the given numbers:
    all_primes = {prime for prime_exponents in all_prime_exponents.values() for prime in prime_exponents}

    # A dictionary mapping each prime to its maximum exponent from all of the numbers:
    prime_to_min_exponent = {
        prime: min([all_prime_exponents[n].get(prime, 0) for n in numbers]) for prime in all_primes
    }

    return math.prod([prime ** min_exponent for prime, min_exponent in prime_to_min_exponent.items()])
