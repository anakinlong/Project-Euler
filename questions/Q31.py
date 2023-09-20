"""
In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).

It is possible to make £2 in the following way:

1 x £1 + 1 x 50p + 2 x 20p + 1 x 5p + 1 x 2p + 3 x 1p

How many different ways can £2 be made using any number of coins?
"""

try:
    import lib
except ModuleNotFoundError:
    from questions import lib


ANSWER = 73682


def n_ways(total: int, coin_values: list[int]) -> int:
    """
    Calculate how many different ways you can sum any number of the given coin values to make the given total.

    This function is just here so that the profiler isn't applied to a recursive function.

    :param total: the total value each sum has to equal.
    :param coin_values: a list of the value of each coin that can be used in the sum.

    :return: the total number of different sums.
    """
    # If there are no coin values, then there are zero different ways of summing them to the total:
    if not coin_values:

        return 0

    # Otherwise, we extract the smallest coin in the list:
    coin, coin_values = coin_values[0], coin_values[1:]
    count = 0

    # TODO remember why % works here
    if total % coin == 0:
        count += 1

    # For the possible number of times we could add this coin to the current total:
    for amount in range(0, total, coin):
        # Count the number of ways we can add other coins to that total to equal the target total:
        count += n_ways(total - amount, coin_values)

    return count


@lib.profiling.profileit()
def main(total: int, coin_values: list[int]) -> int:
    """
    Calculate how many different ways you can sum any number of the given coin values to make the given total.

    :param total: the total value each sum has to equal.
    :param coin_values: a list of the value of each coin that can be used in the sum.

    :return: the total number of different sums.
    """
    # Sorting the coin values from largest to smallest improves speed:
    coin_values.sort(reverse=True)

    return n_ways(total, coin_values)


if __name__ == '__main__':

    answer = main(200, [1, 2, 5, 10, 20, 50, 100, 200])
