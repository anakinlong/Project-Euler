"""
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves
prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""

try:
    import lib
except ModuleNotFoundError:
    from questions import lib


ANSWER = 55


def rotations(n: int) -> list[int]:
    """
    Return a list of all the permutations of the digits of n which can be created by shifting.

    :param n: an integer.

    :return: a list of integers.
    """
    string_n = str(n)
    n_digits = len(string_n)

    # We use a set so that we don't count repeats:
    return list({int(string_n[i:] + string_n[:i]) for i in range(n_digits)})


def prime_sieve_dict(n: int) -> dict[int, bool]:
    """
    Create a dictionary mapping all integers less than or equal to n to whether they are prime or not.

    :param n: an integer.

    :return: a dictionary mapping all integers less than or equal to n to whether they are prime or not.
    """
    # We use a dictionary mapping all numbers to a bool of whether they are prime, since appending to a list would be
    # slow. This way we can have a dictionary of known size and then decide whether each number is prime.
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

    return primes


@lib.profiling.profileit()
def number_of_circular_primes(max_excl: int) -> int:
    """
    Count how many circular primes there are below a maximum value:

    :param max_excl: the maximum (exlcusive) search value.

    :return: the number of circular primes.
    """
    # A dictionary mapping all numbers to whether they are prime:
    primes_dict = prime_sieve_dict(max_excl)
    # A list of just the prime numbers from that dictionary:
    primes = [k for k, is_prime in primes_dict.items() if is_prime]
    count = 0
    found = set()
    for n in primes:
        # If n is prime and we haven't already counted one of its rotations:
        if n not in found:
            # Find all the numbers which are rotations of n and check whether each is prime:
            rotations_n = rotations(n)
            if all(primes_dict[x] for x in rotations_n):
                # Add all of the rotations of n to the count:
                count += len(rotations_n)
                # Add all the rotations of n to the set of found numbers too so we don't double count them:
                {found.add(x) for x in rotations_n}

    return count


if __name__ == '__main__':

    answer = number_of_circular_primes(int(1e6))
