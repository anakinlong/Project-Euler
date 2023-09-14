'''The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, 
contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?'''

from eulerfuncs import *

def n_term_prime_sum(prime_max_incl, n_terms):
    primes = prime_sieve(prime_max_incl)
    result = []
    for i in range(0, len(primes) + 1 - n_terms):
        potential_prime = sum(primes[i:i + n_terms])
        if is_prime(float(potential_prime)) == True:
            if potential_prime <= prime_max_incl:
                result.append(potential_prime)
    return result

def long_sum_search(prime_max_incl, min_n_terms_incl, max_n_terms_incl):
    for i in range(min_n_terms_incl, max_n_terms_incl + 1):
        print(f'Primes able to be written as the sum of {i} consecutive primes:')
        print(n_term_prime_sum(prime_max_incl, i))

if __name__ == '__main__':
    #print(n_term_prime_sum(1000, 21))
    long_sum_search(1000000, 531, 550)