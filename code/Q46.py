'''What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?'''

from eulerfuncs import *

def squares(max_incl):
    '''Returns a list of all the square numbers less than or equal to max_incl.'''
    squares_list = [i * i for i in range(1, int(max_incl ** (1/2)) + 1)]
    return squares_list

def sums(prime_max_incl, square_max_incl):
    primes_list = prime_sieve(prime_max_incl)
    squares_list = squares(square_max_incl)
    odds = dict()
    for i in range(3, prime_max_incl + 2 * square_max_incl + 1, 2):
        odds[i] = False
    for i in prime_sieve(prime_max_incl + 2 * square_max_incl + 1):
        odds[i] = True
    for p in primes_list:
        for s in squares_list:
            odds[p + 2 * s] = True
    return [i for i in odds if odds[i] == False]

# Could code it so that if the min value is less than all the primes and squares checked it'll terminate but cba

if __name__ == '__main__':
    #print(prime_sieve(100))
    #print(squares(100))
    print(min(sums(100000, 100000)))