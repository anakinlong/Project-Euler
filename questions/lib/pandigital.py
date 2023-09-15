"""
Things relating to pandigital numbers.
"""


def is_pandigital(n: int) -> bool:
    """
    Check whether an integer is pandigital - if it has k digits, then it must contain each digit from 1 to k exactly
    once.

    Note that this definition of pandigital numbers differs from that on wikipedia:
    https://en.wikipedia.org/wiki/Pandigital_number

    :param n: an integer.

    :return: True if n is pandigital, otherwise False.
    """
    # We do this by simply counting how many of each digit it contains.
    # First separate n into its digits:
    n_as_digits = [int(digit) for digit in str(n)]
    n_digits = len(n_as_digits)

    # Then count how many of each there are:
    digit_count = {k: 0 for k in range(1, n_digits + 1)}

    for digit in n_as_digits:
        # If the digit is zero, then we are done:
        if digit == 0:
            return False
        # Otherwise, add one to this digit's count:
        else:
            digit_count[digit] += 1

    # If all digits have a count of 1, then n is pandigital:
    if all(count == 1 for count in digit_count.values()):
        return True
    else:
        return False
