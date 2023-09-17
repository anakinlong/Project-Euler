"""
The following iterative sequence is defined for the set of positive integers:

n -> n / 2 (n is even)
n -> 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1.

It can be seen this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet
(Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

Note: Once the chain starts the terms are allowed to go above one million.
"""

from functools import lru_cache

try:
    import lib
except ModuleNotFoundError:
    from questions import lib


ANSWER = 837799


def next_collatz_term(n: int) -> int:
    """
    Return the next term in a Collatz sequence.

    :param n: an integer.

    :return: the next term in a Collatz sequence.
    """
    return int(n / 2) if n % 2 == 0 else int(3 * n + 1)


@lru_cache(maxsize=None)
def find_chain_length(n: int) -> int:
    """
    Find out how long the Collatz chain starting at the number n is.

    :param n: an integer.
    :param cache:

    :return: the length of the Collatz chain starting at the n.
    """
    length = 1
    # Calculate the next term in the chain and add 1 to the length of that term's chain:
    if n > 1:
        n = next_collatz_term(n)
        length += find_chain_length(n)

    return length


@lib.profiling.profileit()
def find_longest_chain(max_excl: int) -> int:
    """
    Find the starting term, below a maximum value, which produces the longest Collatz chain.

    :param max_excl: the maximum (exclusive) value of the starting term.

    :return: the starting term with the longest chain.
    """
    longest_chain_length = 0
    winning_starting_term = 0

    for n in range(1, max_excl):
        length = find_chain_length(n)
        if length > longest_chain_length:
            longest_chain_length = length
            winning_starting_term = n

    return winning_starting_term


if __name__ == '__main__':

    answer = find_longest_chain(int(1e6))
