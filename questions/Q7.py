"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10,001-st prime number?
"""

try:
    import lib
except ModuleNotFoundError:
    from questions import lib


ANSWER = 104743


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


@lib.profiling.profileit()
def nth_prime(n: int) -> int:
    """
    Find the n-th prime number.

    :param n: an integer.

    :return: the n-th prime.
    """
    i = 3
    count = 1
    while count < n:
        if is_prime(i):
            count += 1
        i += 2

    return i - 2


if __name__ == '__main__':

    answer = nth_prime(10001)
