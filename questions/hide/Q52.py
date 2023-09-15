'''It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.'''

def search(min_incl, max_excl):
    for n in range(min_incl, max_excl):
        digits = "".join(sorted(str(n)))
        multiples_digits = []
        for i in range(2, 7):
            multiples_digits.append("".join(sorted(str(i * n))))
        if all(x == digits for x in multiples_digits):
            print(n)

def range_create(power):
    minimum = 10 ** power
    maximum = int((10 ** (power + 1)) / 6)
    return minimum, maximum

if __name__ == '__main__':
    min_incl, max_excl = range_create(5)
    search(min_incl, max_excl)