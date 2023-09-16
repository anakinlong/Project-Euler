"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

try:
    import lib
except ModuleNotFoundError:
    from questions import lib


ANSWER = 142913828922


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


@lib.profiling.profileit()
def sum_of_primes_below_n(n: int) -> int:
    """
    Sum all of the primes below a given value.

    :param n: the maximum value (exclusive).

    :return: the sum of primes.
    """
    # Use a sieve to generate a list of all the primes below n:
    primes = prime_sieve(n - 1)

    return sum(primes)


if __name__ == '__main__':

    answer = sum_of_primes_below_n(int(2e6))
