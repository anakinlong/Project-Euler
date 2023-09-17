"""
Things relating to factors of integers.
"""


def factors(n: int) -> list[int]:
    """
    Return a list of all the factors of n (including 1 and itself).

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
    Count how many factors n has (including 1 and itself).

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


def sum_of_proper_divisors(n: int) -> list[int]:
    """
    Return the sum of all the proper divisors of n (including 1 but not itself).

    :param n: an integer.

    :return: the sum of the proper factors of n.
    """
    # Every number has proper divisor of 1:
    total = 1

    # Now we loop through every integer between 1 and the square root of n to prevent repeats:
    for k in range(2, int(n ** (1 / 2) + 1)):
        # If n is divisible by k, add k to the total:
        if n % k == 0:
            total += int(k)

            # If n / k isn't k, i.e. k isn't the square root of n, also add n / k to the total:
            if int(k) != int(n / k):
                total += int(n / k)

    return total


def amicable_numbers(max_excl: int) -> list[int]:
    """
    Return a list of all the amicable numbers below a specified value.

    :param max_excl: the maximum (exclusive) value of each amicable number.

    :return: a list of all the amicable numbers below max_excl.
    """
    # Starting with an empty list, check whether each number is amicable and add it if it is:
    all_amicable_numbers = []
    for n in range(1, max_excl):
        divisor_sum_n = sum_of_proper_divisors(n)
        # Check whether n is amicable:
        # the sum of its divisors must not equal itself (otherwise it would be a perfect number), and
        # the sum of the divisors of the sum of its divisors must equal itself:
        if divisor_sum_n != n and sum_of_proper_divisors(divisor_sum_n) == n:
            all_amicable_numbers.append(n)

    return all_amicable_numbers


def sum_of_amicable_numbers(max_excl: int) -> list[int]:
    """
    Return a list of all the amicable numbers below a specified value.

    :param max_excl: the maximum (exclusive) value of each amicable number.

    :return: a list of all the amicable numbers below max_excl.
    """
    # Starting with 1, check whether each number is amicable and add tot the total if it is:
    total = 0
    for n in range(1, max_excl):
        divisor_sum_n = sum_of_proper_divisors(n)
        # Check whether n is amicable:
        # the sum of its divisors must not equal itself (otherwise it would be a perfect number), and
        # the sum of the divisors of the sum of its divisors must equal itself:
        if divisor_sum_n != n and sum_of_proper_divisors(divisor_sum_n) == n:
            total += n

    return total
