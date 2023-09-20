"""
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10
are given:

1 / 2 = 0.5
1 / 3 = 0.(3)
1 / 4 = 0.25
1 / 5 = 0.2
1 / 6 = 0.1(6)
1 / 7 = 0.(142857)
1 / 8 = 0.125
1 / 9 = 0.(1)
1 / 10 = 0.1

Where 0.1(6) means 0.1666666..., and has a 1-digit recurring cycle. It can be seen that 1 / 7 has a 6-digit recurring
cycle.

Find that value of d < 1000 for which 1 / d contains the longest recurring cycle in its decimal fraction part.
"""

try:
    import lib
except ModuleNotFoundError:
    from questions import lib


ANSWER = 983


def euler_totient(n: int) -> int:
    """
    Evaluate the Euler totient function at n.

    https://en.wikipedia.org/wiki/Euler%27s_totient_function

    :param n: an integer

    :return: the Euler totient function at n.
    """
    # We start with n:
    product = n

    # Then for each prime factor p of n, we multiply our product by 1 - (1 / p):
    for i in set(lib.primes.prime_factors(n)):
        product *= 1 - (1 / i)

    return int(product)


def cycle_length(denominator: int, base: int) -> int:
    """
    Find the cycle length of the repeating part of the base-imal representation of the fraction 1 / denominator.

    :param denominator: the integer denominator.
    :param base: which base system we are using.

    :return: the cycle length of the fraction.
    """
    totient = euler_totient(denominator)
    for n in lib.factors.factors(totient) + [totient]:
        if base ** n % denominator == 1:

            return n

    return 0


@lib.profiling.profileit()
def find_longest_cycle(max_excl: int, base: int) -> int:
    """
    Find the denominator which gives the longest repeating base-imal representation of 1 / denominator for integer
    denominators less than max_excl.

    :param max_excl: the maximum (exclusive) value of the denominator.
    :param base: which base system we are using.

    :return: the denominator of the longest cycle
    """
    # Find the set of primes that make up the prime factor decomposition of base:
    base_primes = set(lib.primes.prime_factors(base))

    largest = 0
    denominator_of_largest = 0
    for denominator in range(max_excl):
        # The fraction will only have a repeated part if the number is not a multiple of one of the primes in the prime
        # factor decomposition of base:
        if all(denominator % prime != 0 for prime in base_primes):
            # Calculate cycle length and compare to the largest found so far:
            length = cycle_length(denominator, base)
            if length > largest:
                largest = length
                denominator_of_largest = denominator

    return denominator_of_largest


if __name__ == '__main__':

    answer = find_longest_cycle(1000, 10)
