'''Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.'''

def sumOfDigits(n, power):
    digits = str(n)
    total = 0
    for digit in digits:
        total += int(digit) ** power
    return total

def powerSearch(maxExcl, power):
    solutions = []
    for n in range(2, maxExcl):
        if sumOfDigits(n, power) == n:
            solutions.append(n)
    print(solutions)

if __name__ == '__main__':
    #sumOfDigits(1634, 4)
    #powerSearch(10000000, 5)