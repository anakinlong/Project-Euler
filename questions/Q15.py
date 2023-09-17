"""
Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, there are exactly 6
routes to the bottom right corner.

How many such routes are there through a 20x20 grid?
"""

import math

try:
    import lib
except ModuleNotFoundError:
    from questions import lib


ANSWER = 137846528820


EXPLANATION = """
My thought process:

For an n x m grid, we know that we will have to move right n times and down m times. The answer to how many different
routes there are is equivalent to the answer to how many different orderings of n of one item and m of another.

Each route will be a list of n + m instructions (right or down), so the only thing that makes each route different is
which indices are right instructions and which are down.

Once we have decided which indices will have (e.g.) right
instructions, there is only one way to fill the remaining indices with the (e.g.) down instructions. Therefore the
number of different routes is equal to the number of ways to choose which n indices of an n + m length list will be
filled with the right instructions.

This is just the number of ways to choose n items from a collection of (n + m).
"""


@lib.profiling.profileit()
def n_routes(n: int, m: int) -> int:
    """
    Calculate how many different routes from the top left to the bottom right of an n x m grid there are if we are only
    allowed to move right and down.

    :param n: the width of the grid.
    :param m: the height of the grid.

    :return: the number of routes.
    """
    return math.comb(n + m, n)


if __name__ == '__main__':

    answer = n_routes(20, 20)
