"""
The decimal number, 585 = 1001001001_{2} (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""

try:
    import lib
except ModuleNotFoundError:
    from questions import lib


ANSWER = 872187


def is_palindrome(n: int | str) -> bool:
    """
    Decide whether an integer is palindromic or not. That is, whether it can be read the same forwards and backwards.

    :param n: an integer. Can be either a string or integer.

    :return: True if n is palindromic, otherwise False.
    """
    # Make sure n is a string:
    n = str(n)

    # Check whether the string version of n reads the same backwards:
    return n == n[::-1]


@lib.profiling.profileit()
def sum_of_palindromic_numbers(max_excl: int) -> int:
    """
    Find the sum of all the numbers below a given maximum which are palindromic in base 10 and base 2.

    :param max_excl: the maximum (exclusive) search value.

    :return: the sum of all the numbers which are palindromic in base 10 and base 2.
    """
    total = 0
    # A number cannot be even and palindromic in base 2 - since it will start with a 1 it must also end with a 1:
    for n in range(1, max_excl, 2):
        if is_palindrome(n):
            # Calculate the binary representation of n:
            binary_n = bin(n).replace("0b", "")  # Have to remove the "0b" prefix to get the pure form
            if is_palindrome(binary_n):
                total += n

    return total


if __name__ == '__main__':

    answer = sum_of_palindromic_numbers(int(1e6))
