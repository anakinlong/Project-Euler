"""
Things related to formatting/processing the inputs from Project Euler.
"""


def pyramid_to_array(string_pyramid: str) -> list[list[int]]:
    """
    Take the string version of a number pyramid/triangle and format it such that each row is a list of numbers, all in
    one bigger list.

    :param string_pyramid: the pyramid as a string.

    :return: the pyramid formatted as a list of lists.
    """
    # Remove the leading and trailing newline characters:
    string_pyramid = string_pyramid.lstrip("\n")
    string_pyramid = string_pyramid.rstrip("\n")

    # Split the whole thing by the newline character, so we have a list of strings:
    split_by_row = string_pyramid.split("\n")

    # Split each row by the space character, so we have a list of lists of strings, then convert each number to an int:
    return [list(map(int, row.split(" "))) for row in split_by_row]
