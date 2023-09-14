'''Find the first four consecutive integers to have four distinct prime factors each. 
What is the first of these numbers?'''

from eulerfuncs import *

def search(n_consec):
    found = False
    n = 1
    while found == False:
        if all(len(set(prime_factors(x))) == n_consec for x in list(range(n, n + n_consec))):
            print(n)
            found = True
        n += 1

if __name__ == '__main__':
    search(4)