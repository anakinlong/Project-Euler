"""
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 1 ^ 4 + 6 ^ 4 + 3 ^ 4 + 4 ^ 4
8208 = 8 ^ 4 + 2 ^ 4 + 0 ^ 4 + 8 ^ 4
9474 = 9 ^ 4 + 4 ^ 4 + 7 ^ 4 + 4 ^ 4

(As a ^ 4 = a is not a sum it is not included.)

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""

try:
    import lib
except ModuleNotFoundError:
    from questions import lib


ANSWER = 443839


def sum_of_digits_to_power(n: int, power: int) -> int:
    """
    Calculate the sum of the digits of an integer, with each digit being raised to a given power.

    :param n: an integer.
    :param power: the integer we raise each digit to.

    :return: the sum of each digit raised to a power.
    """
    # Convert to a string and add each digit:
    digits = str(n)
    total = 0
    for digit in digits:
        total += int(digit) ** power

    return total


def find_maximum_search_value(power: int) -> int:
    """
    Find the largest number you need to search when trying to find all the numbers whose digits to a given power sum to
    exactly the number itself.

    :param power: the power each digit is raised to in the sum.

    :return: an upper bound on the largest number you need to search.
    """
    # Loop through increasing numbers of digits and test whether the maximum power sum of the digits is less than the
    # smallest number with that many digits:
    n_digits = 1
    nine_to_power = 9 ** power
    while True:
        if n_digits * nine_to_power < 10 ** (n_digits - 1):

            return 10 ** n_digits
        n_digits += 1


# TODO extremely slow (~30s)
@lib.profiling.profileit()
def power_search(power: int) -> int:
    """
    Find the sum of all the numbers that can be written as the sum of each of their digits raised to a given power.

    :param power: the power each digit is raised to in the sum.

    :return: the sum of all the numbers that can be written as the sum of each of their digits raised to a given power.
    """
    # We only need to check numbers with up to a certain number of digits, depending on the power:
    max_excl = find_maximum_search_value(power)
    solutions = []
    for n in range(2, max_excl):
        if sum_of_digits_to_power(n, power) == n:
            solutions.append(n)

    return sum(solutions)


if __name__ == '__main__':

    answer = power_search(5)
