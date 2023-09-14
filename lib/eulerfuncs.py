'''A collection of frequently used functions from previous questions.'''

def is_prime(n):
    '''Checks if n is prime.'''
    if n.is_integer() == True:
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
    else:
        return False

def prime_sieve(max_incl):
    '''Returns a list of all primes less than or equal to max_incl.'''
    primes = dict()
    for i in range(2, max_incl + 1): 
        primes[i] = True
    for i in primes:
        multiples = range(i, max_incl + 1, i)
        for f in multiples[1:]:
            primes[f] = False
    return [i for i in primes if primes[i]==True]

def prime_factors(n):
    '''Returns a list of all the prime factors of n (with repeats).'''
    i = 2
    factors = []
    while i <= n ** (1/2):
        if (n % i):
            i = i + 1
        else:
            n = n / i
            factors.append(i)
    if n > 1:
        factors.append(int(n))
    return factors

def is_pandigital(n):
    '''Checks if n is pandigital.'''
    import numpy
    check = numpy.zeros(max(list(map(int, f"{n}"))))
    for digit in str(n):
        if int(digit) != 0:
            check[int(digit) - 1] += 1
    if all(check == numpy.ones(max(list(map(int, f"{n}"))))):
        return True
    else:
        return False

def is_ndigit_pandigital(n, n_digit):
    '''Checks if n is 1-n_digit pandigital.'''
    import numpy
    check = numpy.zeros(n_digit)
    for digit in str(n):
        if int(digit) != 0:
            check[int(digit) - 1] += 1
    if all(check == numpy.ones(n_digit)):
        return True
    else:
        return False

def factorial(n):
    '''Returns the factorial of n.'''
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact

def factors(n):
    '''Returns a list of all the proper factors of n.'''
    factors = [1, int(n)]
    for i in range(2, int(n ** (1/2) + 1)):
        if n % i == 0:
            factors.append(int(i))
            if int(i) != int(n/i):
                factors.append(int(n / i))
    factors.sort()
    return factors

def totient(n):
    '''Returns the value of the Euler Totient function of n.'''
    result = n
    for i in prime_factors(n):
        result *= 1 - (1 / i)
    return result

def triangle_to_array(triangle):
    '''Takes a "Project Euler-Formatted" triangle and returns it nicely in an array.'''
    split_triangle = triangle.split('\n')
    triangle_array = []
    for i in range(len(split_triangle)):
        new_row = list(map(int, split_triangle[i].split(' ')))
        triangle_array.append(new_row)
    return triangle_array

def max_adjacent_sum(triangle_array):
    '''Returns the maximum path sum of a triangle (that has been put in an array).'''
    current_sum = triangle_array[-1]
    for i in range(len(triangle_array) - 2, -1, -1):
        new_sum = triangle_array[i]
        for j in range(len(new_sum)):
            new_sum[j] += max(current_sum[j], current_sum[j+1])
        current_sum = new_sum
    return current_sum[0]

def generate_triangle_numbers(n_terms):
    '''Returns a list of the first n_terms triangle numbers.'''
    triangle_numbers = []
    for n in range(1, n_terms + 1):
        triangle_numbers.append(int(n * (n + 1) / 2))
    return triangle_numbers

def generate_pentagonal_numbers(n_terms):
    '''Returns a list of the first n_terms pentagonal numbers.'''
    pentagonal_numbers = []
    for n in range(1, n_terms + 1):
        pentagonal_numbers.append(int(n * (3 * n - 1) / 2))
    return pentagonal_numbers

def generate_hexagonal_numbers(n_terms):
    '''Returns a list of the first n_terms hexagonal numbers.'''
    hexagonal_numbers = []
    for n in range(1, n_terms + 1):
        pentagonal_numbers.append(int(n * (2 * n - 1)))
    return hexagonal_numbers