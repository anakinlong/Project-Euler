"""
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
"""

try:
    import lib
except ModuleNotFoundError:
    from questions import lib


ANSWER = 669171001


EXPLANATION = """
The values on the north east diagonal are the odd squares, since that is where the last value goes each time we complete
a full square. If the north east diagonal value is i ^ 2, the north west diagonal value in the same layer will be i - 1
less, and similarly the south west value will be i - 1 less than that, and the south east value i - 1 less than that.

All together, the diagonal values of the i-th layer sum to:

k ^ 2 + k ^ 2 - (k - 1) + k ^ 2 - (k - 1) - (k - 1) + k ^ 2 - (k - 1) - (k - 1) - (k - 1)
= 4k ^ 2 - 6(k - 1)
= 4k ^ 2 - 6k + 6,

where k is the i-th odd number.

Substituting k = 2i - 1:

= 4(2i - 1) ^ 2 - 6(2i - 1) + 6
= 4(4i ^ 2 - 4i + 1) - 12i + 6 + 6
= 16i ^ 2 - 16i + 4 -12i + 12
= 16i ^ 2 - 28i + 16

So for an a grid with n layers, we need to sum those values for i in [1, n].

We know that:
- the sum from 1 to n of 1 is n
- the sum from 1 to n of i is n(n + 1) / 2
- the sum from 1 to n of i ^ 2 is n(n + 1)(2n + 1) / 6

So our total diagonal sum will be:

= 16(n(n + 1)(2n + 1) / 6) - 28(n(n + 1) / 2) + 16(n)
= ...
= 2n(8n ^ 2 - 9n + 7) / 3

An n by n grid has (n + 1) / 2 layers, meaning the diagonal sum for an n by n grid is:

(4n ^ 3 + 3n ^ 2 + 8n + 9) / 6

BUT this doesn't work for the first layer, which is just a 1. 16(1 ^ 2) - 28(1) + 16 = 4, so we need to subtract 3 from
our total.

So our final formula is:

(4n ^ 3 + 3n ^ 2 + 8n - 9) / 6
"""


@lib.profiling.profileit()
def diagonal_sum(n: int) -> int:
    """
    Calculate the sum of the diagonal values of a spiral of numbers in an n by n grid.

    :param n: the width of the grid.

    :return: the sum of the diagonal values.
    """
    return int((4 * n ** 3 + 3 * n ** 2 + 8 * n - 9) / 6)


if __name__ == '__main__':

    answer = diagonal_sum(1001)
