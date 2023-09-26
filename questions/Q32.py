"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once.

The product 7254 is unusual, as the identity, 39 x 186 = 7254, containing multiplicand, multiplier, and product is 1
through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
"""

try:
    import lib
except ModuleNotFoundError:
    from questions import lib


ANSWER = 45228


EXPLANATION = """
We only need to check combinations of numbers which, when multiplied together, produce a number which results in the
total number of digits of the entire identity being 9.

If you multiply one number with n digits with another with m digits, the result will either have m + n or m + n - 1
digits. This is because the smallest number you can produce in this way is:
10 ^ (n - 1) * 10 ^ (m - 1) = 10 ^ (n + m - 2) which has n + m - 1 digits,
and the largest number you can produce is smaller than:
10 ^ n * 10 ^ m = 10 ^ (n + m) which has n + m + 1 digits, meaning the largest number must have at most n + m digits.

We are looking for identities which have exactly 9 digits in total, meaning the sum of the digits of the multiplicand,
multiplier, and product must add to 9. This means we need combinations where:
n + m + n + m - 1 = 9,
or n + m + n + m = 9.
The second case can never happen, since 9 is odd and n and m are integers, so we must have that:
2(n + m) - 1 = 9
<=> n = 1 and m = 4, or n = 2 and m = 3 (we don't need to count the symmetric cases, since we don't care about repeats).
"""


def is_pandigital(n: int) -> bool:
    """
    Check whether an integer is pandigital - if it has k digits, then it must contain each digit from 1 to k exactly
    once.

    Note that this definition of pandigital numbers differs from that on wikipedia:
    https://en.wikipedia.org/wiki/Pandigital_number

    :param n: an integer.

    :return: True if n is pandigital, otherwise False.
    """
    # We do this by simply counting how many of each digit it contains.
    # First separate n into its digits:
    n_as_digits = [int(digit) for digit in str(n)]
    n_digits = len(n_as_digits)

    # Then count how many of each there are:
    digit_count = {k: 0 for k in range(1, n_digits + 1)}

    for digit in n_as_digits:
        # If the digit is zero, then we are done:
        if digit == 0:
            return False
        # Otherwise, add one to this digit's count:
        else:
            digit_count[digit] += 1

    # If all digits have a count of 1, then n is pandigital:
    if all(count == 1 for count in digit_count.values()):
        return True
    else:
        return False


@lib.profiling.profileit()
def pandigital_product_search() -> int:
    """
    Find the sum of all the products which can be formed by a 1-9 digit pandigital product.
    """
    # Use a set since we don't care about duplicates:
    pandigital_products = set()
    for a in range(1, 100):
        digits_a = len(str(a))
        for b in range(10 ** (4 - digits_a), 10 ** (5 - digits_a)):
            ab = a * b
            concatenated = str(a) + str(b) + str(ab)
            # Check if it is n digits long and pandigital:
            if len(concatenated) == 9 and is_pandigital(int(concatenated)):
                pandigital_products.add(ab)

    return sum(pandigital_products)


if __name__ == '__main__':

    answer = pandigital_product_search()
