'Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.'
'How many such routes are there through a 20x20 grid?'

from collections import Counter

def nBitBinary(a, n):
    'Converts an integer a into an n-bit binary number.'
    # Print a in binary:
    binary = bin(a).replace('0b','')
    # Reverse the array:
    x = binary[::-1] 
    # Add enough zeros to the end to reach desired length:
    while len(x) < n:
        x += '0'
    # Return to normal orientation:
    binary = x[::-1]
    return(binary)

def nBitBinaryFast(a, n):
    binary = '%0*d' % (n, int(bin(a)[2:]))
    return(binary)

def counting(a, n):
    "Count the 1's and 0's in a binary number, a, and make sure there are an equal number, n, of each."
    binarya = nBitBinaryFast(a, 2*n)
    counted = Counter(binarya)
    zeros = counted['0']
    ones = counted['1']
    if zeros == n:
        if ones == n:
            return True
    else:
        return False

# This method is extremely slow:
def countingRoutes(n):
    'Counts the routes through an nxn grid moving only right and down.'
    maxBinaryNumber = 2 ** (2 * n) - 1
    minBinaryNumber = 2 ** (n + 1) - 1
    routes = 0
    for a in range(1, maxBinaryNumber):
        isRoute = counting(a, n)
        if isRoute == True:
            routes += 1
    print(routes)

# Best method for an nxm grid:
# Problem is equivalent to finding out how many (n+m)-bit binary numbers contain n zeros and m ones.
# This itself is equivalent to finding how many ways there are of choosing n (or m) things from a collection of (n + m).
# The answer to this is (n+m)choose(n) (or equivalently, (n+m)choose(m)).

def factorial(a):
    fact = 1
    for i in range(1, a+1):
        fact *= i
    return fact

def nRoutes(n, m):
    routes = int(factorial(n + m) / (factorial(n) * factorial(m)))
    print(routes)


if __name__ == '__main__':
    #print(nBitBinary(15, 8))
    #print(counting(16, 4))
    #nBitBinaryFast(15, 8)
    nRoutes(20, 20)