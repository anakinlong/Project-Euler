'Find the sum of all the primes below two million.'

import numpy
import time

def isPrime(n):
    if n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, int(n ** (1/2)) + 1, 2):
            if n % i == 0:
                return False
        return True

def sumOfPrimesBelowN(N):
    startTime = time.time()
    sumOfPrimes = 0
    for i in range(2, N):
        if isPrime(i) == True:
            sumOfPrimes += i
    endTime = time.time()
    executionTime = endTime - startTime
    print('Execution time: ' + str(executionTime) + 's')
    print(sumOfPrimes)

if __name__ == '__main__':
    #print(isPrime(1))
    sumOfPrimesBelowN(2000000)