"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable
numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55, and 110; therefore d(220) = 284. The
proper divisors of 284 are 1, 2, 4, 71, and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10,000.
"""

try:
    import lib
except ModuleNotFoundError:
    from questions import lib


ANSWER = 31626


def sum_of_proper_divisors(n: int) -> int:
    """
    Return the sum of all the proper divisors of n (including 1 but not itself).

    :param n: an integer.

    :return: the sum of the proper factors of n.
    """
    # Every number has proper divisor of 1:
    total = 1

    # Now we loop through every integer between 1 and the square root of n to prevent repeats:
    for k in range(2, int(n ** (1 / 2) + 1)):
        # If n is divisible by k, add k to the total:
        if n % k == 0:
            total += int(k)

            # If n / k isn't k, i.e. k isn't the square root of n, also add n / k to the total:
            if int(k) != int(n / k):
                total += int(n / k)

    return total


# TODO I feel like this could be faster - we should be able to also add divisor_sum_n to the total each time at least
# TODO I have a rough sketch for another solution - not sure if it would be better or not:
# Use a prime sieve to find all primes less than max_excl / 2.
# Loop through the numbers 1 to max_excl - 1:
#   Calculate the prime factor decomposition {prime: exponent} for each using the list of primes
#       (the line above is the part I am least sure about, not sure if there is a fast way of finding the decomposition)
#   The sum of all the factors of a number is:
#       product_{k}(sum_{i=0}^{exponent}(prime_{k}^i))
#       (i.e. the product of the sum of all the powers of each prime up to its exponent in the decomposition)
#       each sum can actually be simplified to:
#           sum_{i=0}^{exponent}(prime_{k}^i) = prime_{k}^{exponent + 1} / (p_{k} - 1)
#   So to get the sum of the proper divisors, just subtract the number from the sum.
@lib.profiling.profileit()
def sum_of_amicable_numbers(max_excl: int) -> list[int]:
    """
    Return a list of all the amicable numbers below a specified value.

    :param max_excl: the maximum (exclusive) value of each amicable number.

    :return: a list of all the amicable numbers below max_excl.
    """
    # Starting with 1, check whether each number is amicable and add tot the total if it is:
    total = 0
    for n in range(1, max_excl):
        divisor_sum_n = sum_of_proper_divisors(n)
        # Check whether n is amicable:
        # the sum of its divisors must not equal itself (otherwise it would be a perfect number), and
        # the sum of the divisors of the sum of its divisors must equal itself:
        if divisor_sum_n != n and sum_of_proper_divisors(divisor_sum_n) == n:
            total += n

    return total


if __name__ == '__main__':

    answer = sum_of_amicable_numbers(int(1e4))
