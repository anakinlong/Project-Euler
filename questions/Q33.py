"""
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly
believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits
in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
"""

import math

try:
    import lib
except ModuleNotFoundError:
    from questions import lib


ANSWER = 100


# TODO this is just a brute force method, could definitely refine but it runs fast enough for now
def fraction_is_simplifiable(numerator: int, denominator: int) -> bool:
    """
    Check whether a fraction could be correctly simplified by cancelling identical digits from both the numerator and
    denominator.

    :param numerator: the integer numerator of the fraction.
    :param denominator: the integer denominator of the fraction.

    :return: True if cancelling identical digits results in a correctly simplified fraction, otherwise False.
    """
    # Calculate the true value of the fraction:
    fraction = numerator / denominator
    string_numerator = str(numerator)
    string_denominator = str(denominator)

    # Try cancelling each combination of the digits:
    for i, numerator_digit in enumerate(string_numerator):
        for j, denominator_digit in enumerate(string_denominator):
            # Both digits must be the same number
            if numerator_digit == denominator_digit:
                # Can't cancel zero at the end of either:
                if not (str(numerator)[i] == '0' and (i == len(str(numerator)) - 1 or j == len(str(denominator)) - 1)):
                    # Create the new numerator and denominator:
                    new_numerator = int(string_numerator[:i] + string_numerator[i+1:])
                    new_denominator = int(string_denominator[:j] + string_denominator[j+1:])
                    # Check if this simplified fraction equals the original:
                    if new_denominator != 0:
                        if new_numerator / new_denominator == fraction:

                            return True

    return False


def greatest_common_divisor(a: int, b: int) -> int:
    """
    Find the greatest common factor of a two integers.

    :param a: an integer.
    :param b: an integer.

    :return: the greatest common factor of a and b.
    """
    while b != 0:
        a, b = b, a % b

    return a


@lib.profiling.profileit()
def fraction_finder(min_incl: int, max_excl: int) -> int:
    """
    Search for fractions which can be correctly simplified by cancelling identical digits from both the numerator and
    denominator.

    :param min_incl: the minimum (inclusive) value of the numerator and denominator.
    :param max_excl: the maximum (exclusive) value of the numerator and denominator.

    :return: the simplified denominator of the product of all the fractions found.
    """
    numerators = []
    denominators = []
    for numerator in range(min_incl, max_excl):
        for denominator in range(numerator + 1, max_excl):
            # Check whether it is simplifiable through the cancelling method, and add to the list if so:
            if fraction_is_simplifiable(numerator, denominator):
                numerators.append(numerator)
                denominators.append(denominator)

    # Calculate the product of all of these fractions, then simplify:
    final_numerator = math.prod(numerators)
    final_denominator = math.prod(denominators)

    return int(final_denominator / greatest_common_divisor(final_numerator, final_denominator))


if __name__ == '__main__':

    answer = fraction_finder(10, 100)
