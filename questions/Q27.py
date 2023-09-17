"""

"""
'''Considering quadratics of the form n^2 + an + b, where |a|<1000 and |b|<=1000,
find the product of the coefficients, a and b, 
for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n=0.'''

import numpy

try:
    import lib
except ModuleNotFoundError:
    from questions import lib


ANSWER = "Answer goes here"


def isPrime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, int(numpy.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True


def nPrimesProduced(a, b):
    end = False
    n = 0
    run = 0
    while end == False:
        if isPrime(n ** 2 + a * n + b) == True:
            run += 1
            n += 1
        else:
            end = True
    return run


@lib.profiling.profileit()
def coefficients(aMin, aMax, bMin, bMax):
    longestRun = 0
    bestCoefficients = [0, 0]
    for b in range(1, (bMax + 1)):
        if isPrime(b) == True:
            for a in range(aMin, (aMax + 1)):
                if nPrimesProduced(a, b) > longestRun:
                    bestCoefficients = [a, b]
                    longestRun = nPrimesProduced(a, b)
    print(longestRun, bestCoefficients)


if __name__ == '__main__':

    coefficients(-999, 999, -1000, 1000)
