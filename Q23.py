'''Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.'''
import numpy

def sumProperDivisors(n):
    total = 1
    for i in range(2, int(numpy.sqrt(n) + 1)):
        if n % i == 0:
            total += int(i)
            if int(i) != int(n/i):
                total += n / i
    return(int(total))

def abundantCheck(n):
    if sumProperDivisors(n) > n:
        return True
    else:
        return False

def listAbundants(maxIncl):
    abundants = []
    for n in range(1, maxIncl):
        if abundantCheck(n) == True:
            abundants.append(n)
    return abundants

def findNumbers(maxIncl):
    numbers = list(range(1, (maxIncl + 1)))
    abundants = listAbundants(maxIncl)
    for i in abundants:
        for j in abundants:
            if i + j in numbers:
                numbers.remove(i + j)
    print(sum(numbers))

if __name__ == '__main__':
    #print(abundantCheck(12))
    #listAbundants(28123)
    findNumbers(28123)