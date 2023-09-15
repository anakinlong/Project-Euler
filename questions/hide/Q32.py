'''We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once.
The product 7254 is unusual, as the identity, 39 x 186 = 7254, containing multiplicand, multiplier, 
and product is 1 through 9 pandigital.
Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.'''

from eulerfuncs import *

def productFinder(max_incl, n):
    pandigitalProducts = []
    for a in range(2, max_incl + 1):
        for b in range(2, int(10000 / a) + 1):
            ab = a * b
            concatenated = int(str(a) + str(b) + str(ab))
            if is_ndigit_pandigital(concatenated, n) == True:
                pandigitalProducts.append(ab)
    return set(pandigitalProducts)

if __name__ == '__main__':
    #print(pandigitalCheck(314256, 6))
    print(sum(productFinder(10000, 9)))