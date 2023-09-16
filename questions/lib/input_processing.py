"""
Things related to formatting/processing the inputs from Project Euler.
"""


def grid_to_array(string_grid: str) -> list[list[int]]:
    """
    Take a string of numbers and convert it to a list of lists.

    :param string_grid: the grid as a string.

    :return: the string_grid formatted as a list of lists.
    """
    # Remove the leading and trailing newline characters:
    string_grid = string_grid.lstrip("\n")
    string_grid = string_grid.rstrip("\n")

    # Split the whole thing by the newline character, so we have a list of strings:
    split_by_row = string_grid.split("\n")

    # Split each row by the space character, so we have a list of lists of strings, then convert each number to an int:
    return [list(map(int, row.split(" "))) for row in split_by_row]
