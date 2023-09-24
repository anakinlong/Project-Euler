"""
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left
to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37,
and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

Note: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""

try:
    import lib
except ModuleNotFoundError:
    from questions import lib


ANSWER = 748317


EXPLANATION = """
For a prime to be right to left truncatable, all the digits must be not be even (except the left-most digit, which can
be 2). This is because all the digits will each be exposed on the right hand side in the 1's column eventually, meaning
the result won't be prime if that digit is even (again, except the left-most digit which can be 2).

Being right to left truncatable also requires that the left-most digit is prime.

For a prime to be left to right truncatable, the right-most digit must be prime, and not equal to 2 unless the prime is
2.

The right to left truncatable primes are going to be rarer, due to the stricter conditions on the digits, so we can
build a list of those and check whether each one is left to right truncatable.
"""


def find_left_truncatable_primes() -> set[int]:
    """
    Find all the primes which are right to left truncatable.

    :return: the set of all left truncatable primes.
    """
    # Start with the left-most digit, which must be prime (2, 3, 5, or 7):
    primes = {2, 3, 5, 7}
    # The set of odd 1 digit integers:
    odds = {"1", "3", "5", "7", "9"}

    def find_extra_digit_primes(current_primes: set[int]) -> set[int]:
        """
        Take a set of prime numbers, and return all the primes which can be formed by adding extra digits to the right
        hand side of each of those primes.

        :param current_primes: a set of prime numbers.

        :return: all the primes which can be formed by adding extra digits to the right hand side of each of those
        primes, including the primes themselves.
        """
        # Take a copy of the current list of primes:
        out_primes = current_primes
        # For each prime, add an odd digit to the end, and test which of these results are prime:
        for prime in current_primes:
            potential_primes = {int(str(prime) + odd) for odd in odds}
            primes_to_add = {p for p in potential_primes if lib.primes.is_prime(p)}
            # Start the process again with only these new primes:
            recursive_primes_to_add = find_extra_digit_primes(primes_to_add)
            # Add all the primes found to our original set of primes:
            out_primes = out_primes.union(recursive_primes_to_add)

        return out_primes

    return find_extra_digit_primes(primes)


def truncate_right(n: int) -> list[int]:
    """
    Return a list of all the integers formed by removing each digit of n from left to right.

    :param n: an integer.

    :return: a list of integers.
    """
    digits = str(n)
    n_digits = len(digits)

    return [int(digits[i + 1:]) for i in range(n_digits - 1)]


def is_right_truncatable_prime(p: int) -> bool:
    """
    Decide whether a prime is right truncatable - that is, whether it is possible to continuously remove digits from
    left to right and have the result still be prime.

    :param p: a prime number.

    :return: True if p is right truncatable, otherwise False.
    """
    return all(lib.primes.is_prime(truncate) for truncate in truncate_right(p))


@lib.profiling.profileit()
def sum_of_truncatable_primes() -> int:
    """
    Find the sum of all the primes which are truncatable left to right and right to left.

    :return: the sum of all the truncatable primes.
    """
    # Find all primes which are right to left truncatable:
    left_truncatable_primes = find_left_truncatable_primes()

    # Only keep the ones which are left to right truncatable:
    truncatable_primes = {p for p in left_truncatable_primes if is_right_truncatable_prime(p)}

    # Remove 2, 3, 5, and 7 because it doesn't fit our definition:
    {truncatable_primes.discard(n) for n in {2, 3, 5, 7}}

    return sum(truncatable_primes)


if __name__ == '__main__':

    answer = sum_of_truncatable_primes()
