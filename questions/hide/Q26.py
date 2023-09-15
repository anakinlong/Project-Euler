'''Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.'''

import numpy

def prime_factors(n):
    i = 2
    factors = []
    while i <= numpy.sqrt(n):
        if (n % i):
            i = i + 1
        else:
            n = n / i
            factors.append(i)
    if n > 1:
        factors.append(int(n))
    return set(factors)

def totient(n):
    result = n
    for i in prime_factors(n):
        result *= 1 - (1 / i)
    return result

def factors(n):
    factors = [1, int(n)]
    for i in range(2, int(n ** (1/2) + 1)):
        if n % i == 0:
            factors.append(int(i))
            if int(i) != int(n/i):
                factors.append(int(n / i))
    factors.sort()
    return factors

def cycle_length(denominator):
    for n in factors(totient(denominator)):
        if 10 ** n % denominator == 1:
            return n
    return 0
        
def cycle_search(max_excl):
    max_cycle_length = 0
    max_cycle_denominator = 0
    for d in range(max_excl):
        if all(d % x != 0 for x in [2, 5]):
            if cycle_length(d) > max_cycle_length:
                max_cycle_length = cycle_length(d)
                max_cycle_denominator = d
    print(max_cycle_length, max_cycle_denominator)

if __name__ == '__main__':
    #print(prime_factors(2520))
    #print(totient(20))
    #print(factors(20))
    #print(cycle_length(167))
    cycle_search(1000)