"""
Things relating to factors of integers.
"""


def factors(n: int) -> list[int]:
    """
    Return a list of all the proper factors of n.

    :param n: an integer.

    :return: the proper factors of n.
    """
    # TODO use something better than lists, since you don't know how long the list will be
    # Every number has proper factors of 1 and itself:
    all_factors = [1, int(n)]

    # Now we loop through every integer between 1 and the square root of n to prevent repeats:
    for k in range(2, int(n ** (1 / 2) + 1)):
        # If n is divisible by k, add k to the list of proper factors:
        if n % k == 0:
            all_factors.append(int(k))

            # If n / k isn't k, i.e. k isn't the square root of n, also add n / k to the list of factors:
            if int(k) != int(n / k):
                all_factors.append(int(n / k))

    # Sort the list from smallest to largest:
    all_factors.sort()

    return all_factors


def count_factors(n: int) -> int:
    """
    Count how many proper factors n has.

    :param n: an integer.

    :return: the number of proper factors of n.
    """
    # Every number has proper factors of 1 and itself:
    n_factors = 2

    # Now we loop through every integer between 1 and the square root of n to prevent repeats:
    for k in range(2, int(n ** (1 / 2) + 1)):
        # If n is divisible by k, add k to the list of proper factors:
        if n % k == 0:
            n_factors += 1

            # If n / k isn't k, i.e. k isn't the square root of n, also add n / k to the list of factors:
            if int(k) != int(n / k):
                n_factors += 1

    return n_factors
