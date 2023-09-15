'2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.'
'What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?'
import numpy
def primeFactors(number):
    i = 2
    factors = []
    while i <= numpy.sqrt(number):
        if (number % i):
            i = i + 1
        else:
            number = number / i
            factors.append(i)
    if number > 1:
        factors.append(int(number))
    return(factors)

def primeExponents(number):
    factors = primeFactors(number)
    primes = list(set(factors))
    exponents = []
    for i in primes:
        exponents.append(factors.count(i))
    return(primes, exponents)

def lowestCommonMultiple(numbers):
    lcmPrimes = []
    for i in numbers:
        primes, exponents = primeExponents(i)
        for j in primes:
            if j not in lcmPrimes:
                lcmPrimes.append(j)
    lcmPrimes.sort()
    exponentsArray = numpy.zeros([len(numbers), len(lcmPrimes)])
    for i in numbers:
        factors = primeFactors(i)
        for j in lcmPrimes:
            exponent = factors.count(j)
            if exponent != 0:
                numberIndex = numbers.index(i)
                primeIndex = lcmPrimes.index(j)
                exponentsArray[numberIndex][primeIndex] = exponent
    maxExponents = numpy.zeros(len(lcmPrimes))
    for j in range(len(lcmPrimes)):
        maxExponents[j] = max(exponentsArray[:,j])

    lcm = 1
    for j in range(len(lcmPrimes)):
        lcm = lcm * (lcmPrimes[j] ** maxExponents[j])

    print(lcmPrimes)
    print(maxExponents)
    print(exponentsArray)
    print(int(lcm))


if __name__ == '__main__':
    lowestCommonMultiple(range(1,21))