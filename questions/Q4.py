"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is
9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

try:
    import lib
except ModuleNotFoundError:
    from questions import lib


ANSWER = 906609


def is_palindrome(n: int) -> bool:
    """
    Decide whether an integer is a palindrome; that is, whether it reads the same left-ro-right and right-to-left.

    :param n: an integer.

    :return: True if n is a palindrome, otherwise False.
    """
    # Turn it into a string and compare to its reversed version:
    return str(n) == str(n)[::-1]


@lib.profiling.profileit()
def palindromes(min_inclusive: int, max_exclusive: int) -> int:
    """
    Find the largest palindrome made from the product of two integers in the interval [min_inclusive, max_exclusive).

    :param min_inclusive: the minimum value of the integers.
    :param min_inclusive: the minimum value of the integers.

    :return: the palindrome with the largest value.
    """
    # TODO use something better than a list
    palindromes = []
    # TODO this is very slow, and wouldn't finish in a reasonable time for much larger problems
    for i in range(min_inclusive, max_exclusive):
        for j in range(min_inclusive, max_exclusive):
            value = i * j
            if is_palindrome(value):
                palindromes.append(value)

    return max(palindromes)


if __name__ == '__main__':

    answer = palindromes(100, 1000)
