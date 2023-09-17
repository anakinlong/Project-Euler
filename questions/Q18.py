"""
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top
to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below.

Note: As there are only 16384 routes, it is possible to solve this problem by trying every route. However, Problem 67,
is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a
clever method! ;o)
"""

try:
    import lib
except ModuleNotFoundError:
    from questions import lib


ANSWER = 1074


TRIANGLE = """
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
"""


@lib.profiling.profileit()
def max_adjacent_sum(triangle: str) -> int:
    """
    Calculate the maximum total resulting from a path of adjacent numbers from the top of the triangle to the bottom.

    :param triangle: the triangle in string form.

    :return: the sum of the values in the maximum path.
    """
    # Convert the triangle into a list of lists of ints, with each row being a list:
    triangle_array = lib.input_processing.grid_to_array(triangle)
    n_rows = len(triangle_array)

    # Starting with the bottom row of the triangle:
    current_row = triangle_array[-1]
    # Loop through each row of the triangle from the second to last upwards:
    for i in range(n_rows - 2, -1, -1):
        row_above = triangle_array[i]
        # For each number in the row above, we choose which path we would like to follow below it.
        # The options are the optimal paths from each of the adjacent numbers below:
        for j in range(len(row_above)):
            row_above[j] += max(current_row[j], current_row[j + 1])
        # Set the current row to the row above, ready for the next iteration:
        current_row = row_above

    # Once the loop is complete, the "current row" should just be the top row of the triangle with the maximum possible
    # total:
    return current_row[0]


if __name__ == '__main__':

    answer = max_adjacent_sum(TRIANGLE)
