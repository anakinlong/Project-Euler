'''The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
How many circular primes are there below one million?'''

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

def rotations(n):
    nRotations = len(str(n))
    rotationsArray = []
    for i in range(0, nRotations):
        newNumber = ''
        for j in range(0, nRotations):
            newNumber += str(n)[(i+j) % nRotations]
        rotationsArray.append(int(newNumber))
    return rotationsArray

def circularSearch(maxExcl):
    total = 0
    for n in range(2, maxExcl):
        if isPrime(n) == True:
            rotationsArray = rotations(n)
            if all(isPrime(x) == True for x in rotationsArray):
                total += 1
    print(total)

if __name__ == '__main__':
    #print(rotations(197))
    circularSearch(1000000)