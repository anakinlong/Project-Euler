'''The number 3797 has an interesting property. Being prime itself, 
it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. 
Similarly we can work from right to left: 3797, 379, 37, and 3.
Find the sum of the only eleven primes that are both truncatable from left to right and right to left.'''

def isPrime(n):
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

def truncateLeft(n):
    digits = str(n)
    truncatedsArray = []
    for i in range(len(digits) - 1):
        truncated = digits[i + 1: :]
        truncatedsArray.append(int(truncated))
    return truncatedsArray

def truncateRight(n):
    digits = str(n)
    truncatedsArray = []
    for i in range(len(digits) - 1):
        truncated = digits[0: i + 1:]
        truncatedsArray.append(int(truncated))
    return truncatedsArray

def primeSearch(maxExcl):
    primes = []
    for n in range(10, maxExcl):
        if isPrime(n) == True:
            if all(isPrime(x) == True for x in truncateLeft(n)):
                if all(isPrime(y) == True for y in truncateRight(n)):
                    primes.append(n)
    print(primes)
    print(sum(primes))

if __name__ == '__main__':
    #print(isPrime(1))
    #print(truncateLeft(3797))
    #print(truncateRight(3797))
    primeSearch(1000000)