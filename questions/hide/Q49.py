'''The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, 
is unusual in two ways: (i) each of the three terms are prime, 
and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes 
exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?'''

from eulerfuncs import *

def search():
    for a in range(1000, 9997):
        for d in range(1, int((9999 - a) / 2) + 1):
            if sorted(list(str(a))) == sorted(list(str(a + d))) and sorted(list(str(a))) == sorted(list(str(a + 2 * d))):
                if all(is_prime(float(x)) == True for x in [a, a + d, a + 2 * d]):
                    print([a, a + d, a + 2 * d])

if __name__ == '__main__':
    #a = '2387956'
    #print(sorted(list(str(a))))
    search()