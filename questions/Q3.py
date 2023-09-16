"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""

try:
    import lib
except ModuleNotFoundError:
    from questions import lib


ANSWER = 6857


@lib.profiling.profileit()
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


if __name__ == '__main__':

    answer = prime_factors(600851475143)
