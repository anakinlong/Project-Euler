'''Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed.
What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?'''
import numpy

def createSpiral(n):
    spiralArray = numpy.zeros([n, n])
    spiralArray[int((n-1)/2)][int((n-1)/2)] = 1
    print(spiralArray)
    # cba

def addDiagonals(n):
    # Top right diagonal:
    TRsum = 0
    for i in range(1, int((n+1)/2)):
        TRsum += ((2 * i + 1) ** 2)
    
    # Top left diagonal:
    TLsum = 0
    for i in range(1, int((n+1)/2)):
        TLsum += ((2 * i + 1) ** 2 - 2 * i)

    # Bottom right diagonal:
    BRsum = 0
    for i in range(1, int((n+1)/2)):
        BRsum += ((2 * i + 1) ** 2 - 4 * i)
    
    # Bottom left diagonal:
    BLsum = 0
    for i in range(1, int((n+1)/2)):
        BLsum += ((2 * i + 1) ** 2 - 6 * i)

    total = 1 + TRsum + TLsum + BRsum + BLsum
    print(total)

if __name__ == '__main__':
    #createSpiral(5)
    addDiagonals(1001) 