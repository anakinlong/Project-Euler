"""
Things relating to factors of integers.
"""


def factorial(n: int) -> int:
    """
    Return the factorial of n.

    :param n: an integer.

    :return: n factorial.
    """
    # Starting with 1, we multiply by all the integers up to n inclusive:
    product = 1

    for k in range(2, n + 1):
        product *= k

    return product


def factors(n: int) -> list[int]:
    """
    Return a list of all the proper factors of n.

    :param n: an integer.

    :return: the proper factors of n.
    """
    # TODO use something better than lists, since you don't know how long the list will be
    # Every number has proper factors of 1 and itself:
    factors = [1, int(n)]

    # Now we loop through every integer between 1 and the square root of n to prevent repeats:
    for k in range(2, int(n ** (1 / 2) + 1)):
        # If n is divisible by k, add k to the list of proper factors:
        if n % k == 0:
            factors.append(int(k))

            # If n / k isn't k, i.e. k isn't the square root of n, also add n / k to the list of factors:
            if int(k) != int(n / k):
                factors.append(int(n / k))

    # Sort the list from smallest to largest:
    factors.sort()

    return factors
