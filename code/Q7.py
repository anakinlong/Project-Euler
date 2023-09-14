'By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.'
'What is the 10 001st prime number?'
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
        factors.append(number)
    return(factors)

def nthPrime(n):
    primes = []
    i = 1
    count = 0
    while count < n:
        if (len(primeFactors(i)) == 1):
            primes.append(i)
            count += 1
        i += 1
    print(primes)

if __name__ == '__main__':
    nthPrime(10001)