"""
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 x d10 x d100 x d1000 x d10000 x d100000 x d1000000
"""

try:
    import lib
except ModuleNotFoundError:
    from questions import lib


ANSWER = 210


@lib.profiling.profileit()
def product_of_digits(indices: list[int]) -> int:
    """
    Calculate the product of the digits at the given indices of the number formed by concatenating the integers starting
    at 1 in ascending order.

    :param indices: an list of indices (0 indexed).

    :return: the product of specific digits of the concatenated number.
    """
    # Loop through each number in the concatenation and see whether it contains any of the digits we are interested in:
    position = -1
    number = 1
    total = 1
    # Whether we have counted each index or not:
    counted = {i: False for i in indices}
    # Don't go beyond the highest index:
    final_index = max(indices)

    while position <= final_index:
        string_number = str(number)
        # Set our current position to be the end of the current number:
        position += len(string_number)
        # The indices we haven't counted yet which are lower than our current position:
        indices_in_this_number = [i for i in indices if not counted[i] and position >= i]
        for i in indices_in_this_number:
            # Multiply by each and mark as counted:
            total *= int(string_number[-1 - (position - i)])
            counted[i] = True
        number += 1

    return total


if __name__ == '__main__':

    answer = product_of_digits([0, 9, 99, 999, 9999, 99999, 999999])
