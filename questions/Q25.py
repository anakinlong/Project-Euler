'''What is the index of the first term in the Fibonacci sequence to contain 1000 digits?'''

try:
    import lib
except ModuleNotFoundError:
    from questions import lib


ANSWER = 4782


def number_of_digits(n: int) -> int:
    """
    Return the number of digits n has.

    :param n: an integer.

    :return: the number of digits.
    """
    return len(str(n))


@lib.profiling.profileit()
def find_first_n_digit_fibonacci(n_digits: int, a_1: int, a_2: int) -> int:
    """
    Calculate first Fibonacci number to contain at least n_digits digits.

    :param n_digits: how many digits we are aiming for.
    :param a_1: the first term of the sequence.
    :param a_2: the second term of the sequence.

    :return: the first Fibonacci number with the specified number of  digits.
    """
    # Check whether the first or second term meets the required number of digits:
    for index, term in {1: a_1, 2: a_2}.items():
        if number_of_digits(term) >= n_digits:
            return index

    # If not, then we will have to calculate subsequent terms and test whether each has the required number of digits:
    previous_term = a_1
    current_term = a_2
    index = 2
    while True:
        # Calculate the next term:
        index += 1
        current_term, previous_term = current_term + previous_term, current_term

        if number_of_digits(current_term) >= n_digits:

            return index


if __name__ == '__main__':

    answer = find_first_n_digit_fibonacci(1000, 1, 1)
