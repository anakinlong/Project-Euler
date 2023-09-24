"""
Take the number 192 and multiply it by each of 1, 2, and 3:

192 x 1 = 192
192 x 2 = 384
192 x 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576.

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645,
which is the concatenated product of 9 and (1, 2, 3, 4, 5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with
(1,2, ... , n) where n > 1?
"""

try:
    import lib
except ModuleNotFoundError:
    from questions import lib


ANSWER = 932718654


@lib.profiling.profileit()
def find_maximum_concatenated_products() -> int:
    """
    Find the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with
    (1,2, ... , n) where n > 1.

    :return: the largest value found.
    """
    best = 0
    # Since we need to at least take 2 products and concatenate them, the number is at most 4 digits long:
    for n in range(1, int(1e4)):
        # Calculate all multiples, then concatenate until the result is 9 digits or longer:
        products = [str(n * x) for x in range(1, 10)]
        concatenated_products = ""
        n_digits = 0
        i = 0
        while n_digits < 9:
            new_digits = products[i]
            concatenated_products += new_digits
            n_digits += len(new_digits)
            i += 1
        # If the result is 9 digits long, larger than the current best, and pandigital, set it as our new largest:
        if n_digits == 9:
            new_value = int(concatenated_products)
            if new_value > best and lib.pandigital.is_pandigital(new_value):
                best = new_value

    return best


if __name__ == '__main__':

    answer = find_maximum_concatenated_products()
