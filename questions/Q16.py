"""
2 ^ 15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2 ^ 1000?
"""

try:
    import lib
except ModuleNotFoundError:
    from questions import lib


ANSWER = 1366


@lib.profiling.profileit()
def sum_of_digits(n: int) -> int:
    """
    Calculate the sum of the digits of an integer.

    :param n: an integer.

    :return: the sum of its digits.
    """
    # Convert to a string and add each digit:
    digits = str(n)
    total = 0
    for digit in digits:
        total += int(digit)

    return total


if __name__ == '__main__':

    answer = sum_of_digits(2 ** 1000)
