'''What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product 
of an integer with (1,2, ... , n) where n > 1?'''

import numpy

def is_pandigital(n, n_digits):
    if len(str(n)) == n_digits:
        check = numpy.zeros(n_digits)
        for digit in str(n):
            if int(digit) != 0:
                check[int(digit) - 1] += 1
        if all(check == numpy.ones(n_digits)):
            return True
        else:
            return False
    else:
        return False

def find(max_excl=10000):
    best = 0
    for n in range(1, max_excl):
        for i in range(3, 10):
            products = [n * x for x in range(1, i)]
            max_concatenated = ''
            for number in products:
                max_concatenated += str(number)
            if is_pandigital(int(max_concatenated), 9) == True:
                if int(max_concatenated) > best:
                    best = int(max_concatenated)
    return best


if __name__ == '__main__':
    #print(is_pandigital(43120567, 8))
    #print(sorted([10 * x for x in range(1, 20)], key=str)[::-1])
    print(find(10000))