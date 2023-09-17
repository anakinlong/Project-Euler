"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19
letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

Note: do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one
hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""

try:
    import lib
except ModuleNotFoundError:
    from questions import lib


ANSWER = 21124


# Dictionaries mapping combinations of digits to the words they represent:
ONES = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
}

TEENS = {
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
}

TENS = {
    2: "twenty",
    3: "thirty",
    4: "forty",
    5: "fifty",
    6: "sixty",
    7: "seventy",
    8: "eighty",
    9: "ninety",
}


def number_to_words(n: int, sep: str = " ") -> str:
    """
    Convert an integer number to written format. Only supports numbers in the range [1, 2000).

    :param n: an integer.
    :param sep: the string used to separate each word. Defaults to a space.

    :return: the input number written using words.
    """
    # Convert the integer to a dictionary mapping each power of ten's exponent to its digit value.
    # e.g. 1405 -> {0: 5, 1: 0, 2: 4, 3: 1}.
    # We have to reverse the string in order for this to work:
    digits_of_n = {i: int(str(n)[::-1][i]) for i in range(len(str(n)))}

    # A dictionary of whether we have each power:
    have = {
        "thousands": digits_of_n.get(3, None) not in [None, 0],
        "hundreds": digits_of_n.get(2, None) not in [None, 0],
        "tens": digits_of_n.get(1, None) not in [None, 0],
        "ones": digits_of_n.get(0, None) not in [None, 0],
    }

    # Now use these dictionaries to build the written form of this number:
    words = []

    # Thousands:
    if have["thousands"]:
        words.append(ONES[digits_of_n[3]])
        words.append("thousand")
    # Hundreds:
    if have["hundreds"]:
        words.append(ONES[digits_of_n[2]])
        words.append("hundred")
    # The "and" that comes after this point in numbers over one hundred with further non-zero digits:
    if n >= 100:
        if have["tens"] or have["ones"]:
            words.append("and")
    # Tens:
    # Whether the number ends in a "teen" - since this will affect the ones as well as tens:
    teens = False
    if have["tens"]:
        teens = digits_of_n[1] == 1
        if teens:
            # Turn the tens and ones digits into a "teens" double digit:
            teen = int(str(digits_of_n[1]) + str(digits_of_n[0]))
            words.append(TEENS[teen])
        else:
            words.append(TENS[digits_of_n[1]])
    # Ones:
    if have["ones"]:
        # Only need to add anything if the number doesn't end in "teen":
        if not teens:
            words.append(ONES[digits_of_n[0]])

    # Join each word using a space:
    return sep.join(words)


@lib.profiling.profileit()
def letter_count() -> int:
    total_letters = 0
    for n in range(1, 1001):
        total_letters += len(number_to_words(n, sep=""))

    return total_letters


if __name__ == "__main__":

    answer = letter_count()
