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


ANSWER = "Answer goes here"


@lib.profiling.profileit()
def main() -> int:
    """
    """


def addDiagonals(n):
    # Top right diagonal:
    TRsum = 0
    for i in range(1, int((n+1)/2)):
        TRsum += ((2 * i + 1) ** 2)

    # Top left diagonal:
    TLsum = 0
    for i in range(1, int((n+1)/2)):
        TLsum += ((2 * i + 1) ** 2 - 2 * i)

    # Bottom right diagonal:
    BRsum = 0
    for i in range(1, int((n+1)/2)):
        BRsum += ((2 * i + 1) ** 2 - 4 * i)

    # Bottom left diagonal:
    BLsum = 0
    for i in range(1, int((n+1)/2)):
        BLsum += ((2 * i + 1) ** 2 - 6 * i)

    total = 1 + TRsum + TLsum + BRsum + BLsum
    print(total)


if __name__ == '__main__':

    addDiagonals(1001)
