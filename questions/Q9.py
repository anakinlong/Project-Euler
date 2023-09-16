"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2.

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

try:
    import lib
except ModuleNotFoundError:
    from questions import lib


ANSWER = 31875000


@lib.profiling.profileit()
def triplet(target_sum: int) -> int:
    """
    Return the product of the three integers which make a Pythagorean triple and also sum to the given target value.

    :param target_sum: the integer that the three numbers must sum to.

    :return: the product of the three integers of the Pythagorean triple.
    """
    # TODO there's definitely a smarter way than looping through all combinations
    # Loop through all possible combinations of a, b, and c:
    for a in range(1, target_sum - 1):
        for b in range(1, target_sum - a):
            c = target_sum - a - b

            # If this is a Pythagorean triple, return it:
            if (a ** 2 + b ** 2 == c ** 2):

                return a * b * c


if __name__ == '__main__':

    answer = triplet(1000)
