"""
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names,
begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value
by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the
938th name in the list. So, COLIN would obtain a score of 938 x 53 = 49714.

What is the total of all the name scores in the file?
"""

import pathlib

try:
    import lib
except ModuleNotFoundError:
    from questions import lib


ANSWER = 871198282


# The letters of the alphabet in alphabetical order:
LETTERS = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
    "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
]

# A dictionary mapping each letter of the alphabet to its score:
LETTERS_TO_SCORES = {letter: index + 1 for index, letter in enumerate(LETTERS)}

# The filepath to names.txt:
NAMES_FILE_PATH = lib.MATERIALS.joinpath("names.txt")


def alphabetical_value(name: str, letters_to_scores: dict[str, int]) -> int:
    """
    Calculate the alphabetical value of a string name.

    :param name: a string.
    :param letters_to_scores: a dictionary mapping letters to their score.

    :return: the sum of the alphabetical positions of each letter in the name.
    """
    # Loop through each letter an add its score to the total:
    total = 0
    for letter in name:
        total += letters_to_scores[letter]

    return total


def read_names_file(file_path: pathlib.Path) -> list[str]:
    """
    Read and process a file containing a list of names into a list of string names.

    :param file_path: the path to the text file.

    :return: a list of string names.
    """
    # Open the text file and read the contents as one long string:
    with open(file_path, 'r') as file:
        file_content = file.read()

    # Split the content into a list of names, removing the quotes and leading/trailing quotation marks:
    return [name.strip('"') for name in file_content.split(",")]


@lib.profiling.profileit()
def total_file_score(file_path: pathlib.Path, letters_to_scores: dict[str, int]) -> int:
    """
    Calculate the total score of all the name scores in the given list of names.

    :param file_path: the path to the text file containing the list of names.
    :param letters_to_scores: a dictionary mapping letters to their score.

    :return: the total score.
    """
    # Read in the names file, convert it to a list of names, and sort alphabetically:
    names_list = read_names_file(file_path)
    names_list.sort()

    # Loop through each name and add its score to the total:
    total = 0
    for index, name in enumerate(names_list):
        score = (index + 1) * alphabetical_value(name, letters_to_scores)
        total += score

    return total


if __name__ == '__main__':

    answer = total_file_score(NAMES_FILE_PATH, LETTERS_TO_SCORES)
