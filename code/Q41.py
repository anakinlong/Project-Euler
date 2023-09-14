'''We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. 
For example, 2143 is a 4-digit pandigital and is also prime.
What is the largest n-digit pandigital prime that exists?'''

import itertools

def isPrime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, int(n ** (1/2)) + 1, 2):
            if n % i == 0:
                return False
        return True

def generatePandigitals(nDigits):
    number = ''
    for i in range(1, nDigits + 1):
        number += str(i)
    pandigitalArrays = list(itertools.permutations(list(number)))
    pandigitalList = []
    for pandigital in pandigitalArrays:
        digits = ''
        for digit in pandigital:
            digits += digit
        pandigitalList.append(int(digits))
    return(pandigitalList)

def pandigitalSearch(maxDigits):
    largestPrime = 0
    for nDigits in range(1, maxDigits + 1):
        pandigitalList = generatePandigitals(nDigits)
        for n in pandigitalList:
            if isPrime(n) == True:
                if n > largestPrime:
                    largestPrime = n
    print(largestPrime)


if __name__ == '__main__':
    #print(generatePandigitals(4))
    pandigitalSearch(9)