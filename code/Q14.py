'Which starting number, under one million, produces the longest Collatz chain?'

def collatzChain(n):
    chain = [int(n)]
    while n > 1:
        if n % 2 == 0:
            n /= 2
            chain.append(int(n))
        else:
            n = 3 * n + 1
            chain.append(int(n))
    return(chain)

def collatzChainLength(n):
    length = 1
    while n > 1:
        if n % 2 == 0:
            n /= 2
            length += 1
        else:
            n = 3 * n + 1
            length += 1
    return(length)

def longestChain(maxExcl):
    longestChain = 0
    longestChainStartingNumber = 0
    for n in range(1, maxExcl):
        length = collatzChainLength(n)
        if length > longestChain:
            longestChain = length
            longestChainStartingNumber = n
    print('Starting Number = ' + str(longestChainStartingNumber) + ', Chain Length = ' + str(longestChain))

if __name__ == '__main__':
    #collatzChain(13)
    #collatzChainLength(13)
    longestChain(10 ** 6)