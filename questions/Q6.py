"""
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385.

The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 3025.

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is,

3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

try:
    import lib
except ModuleNotFoundError:
    from questions import lib


ANSWER = 25164150


def sum_of_squares(numbers: list[int]) -> int:
    """
    Calculate the sum of the square of each number from a list.

    :param numbers: a list of integers.

    :return: the sum of their squares.
    """
    return sum([n ** 2 for n in numbers])


def square_of_sum(numbers: list[int]) -> int:
    """
    Calculate the square of the sum of a list of numbers.

    :param numbers: a list of integers.

    :return: the square of their sum.
    """
    return sum(numbers) ** 2


@lib.profiling.profileit()
def difference(numbers: list[int]) -> int:
    """
    For a given list of numbers, calculate the difference between the sum of their squares and the square of their sum.

    :param numbers: a list of integers.

    :return: the difference between the sum of their squares and the square of their sum.
    """
    numbers_sum_of_squares = sum_of_squares(numbers)
    numbers_square_of_sum = square_of_sum(numbers)

    return abs(numbers_sum_of_squares - numbers_square_of_sum)


if __name__ == '__main__':

    answer = difference(range(1, 101))
