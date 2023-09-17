"""
Euler discovered the remarkable quadratic formula:

n ^ 2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive integer values 0 <= n <= 39. However, when
n = 40, 40 ^ 2 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41 ^ 2 + 41 + 41 is clearly
divisible by 41.

The incredible formula n ^ 2 - 79n + 1601 was discovered, which produces 80 primes for the consecutive values
0 <= n <= 79. The product of the coefficients, -79 and 1601, is -126479.

Considering quadratics of the form:
n ^ 2 + an + b, where |a| < 1000 and |b| <= 1000

where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |-4| = 4

Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes
for consecutive values of n, starting with n = 0.
"""

import math

try:
    import lib
except ModuleNotFoundError:
    from questions import lib


ANSWER = -59231


def number_of_consecutive_primes(a: int, b: int) -> int:
    """
    Find how many consecutive primes are produced by the formula n ^ 2 + an + b, starting from n = 0.

    :param a: the linear coefficient of the formula.
    :param b: the constant term of the formula.

    :return: how many primes in a row are produced.
    """
    # Loop through each value of n, starting at zero, and find out whether the value produced is prime:
    n = 0
    consecutive_primes = 0
    while True:
        if lib.primes.is_prime(n ** 2 + a * n + b):
            consecutive_primes += 1
            n += 1
        else:

            return consecutive_primes


@lib.profiling.profileit()
def find_product_of_best_coefficients(range_a: tuple[int, int], range_b: tuple[int, int]) -> tuple[int, int]:
    """
    Find the product of the integer coefficients, a and b, which produce the most consecutive primes using the formula
    n ^ 2 + an + b, starting from n = 0.

    :param range_a: the minimum and maximum (inclusive) values that a can take.
    :param range_b: the minimum and maximum (inclusive) values that b can take.

    :return: the product of the optimum coefficients.
    """
    # Process inputs:
    a_min, a_max = range_a
    b_min, b_max = range_b
    # b must be positive, since the first number produced is 0 ^ 2 + 0a + b = b:
    b_min = max(b_min, 1)
    # In fact, b must be prime - therefore we will find all of the prime numbers in the range [b_min, b_max]:
    primes_in_range = [prime for prime in lib.primes.prime_sieve(b_max) if prime >= b_min]

    # Loop through combinations of a and b and find the number of consecutive primes produced:
    most_consecutive_primes = 0
    best_coefficients = None, None
    # b must be prime:
    for b in primes_in_range:
        a_min, a_max = range_a
        # a must have the same value mod 2 as b, since the second prime in the run would be 1 + a + b.
        # To create a run of at least length l, a must also be large enough such that:
        #     a >= (2 - b - l ^ 2) / l,
        # since for the l-th term in the run to be prime the term itself must be greater than or equal to 2, i.e.:
        #     l ^ 2 + an + b >= 2.
        # Since we are only interested in runs with a length greater than the current longest run, we can set
        # l = most_consecutive_primes + 1:
        a_min = max(a_min, math.ceil((2 - b - (most_consecutive_primes + 1) ** 2) / (most_consecutive_primes + 1)))
        # Add one if not the same mod 2 as b:
        a_min += 0 if a_min % 2 == b % 2 else 1
        # Loop through in steps of 2:
        for a in range(a_min, a_max + 1, 2):
            consecutive_primes = number_of_consecutive_primes(a, b)

            if consecutive_primes > most_consecutive_primes:
                best_coefficients = a, b
                most_consecutive_primes = consecutive_primes

    return best_coefficients[0] * best_coefficients[1]


if __name__ == '__main__':

    answer = find_product_of_best_coefficients((-999, 999), (-1000, 1000))
