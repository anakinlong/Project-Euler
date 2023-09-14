'What is the value of the first triangle number to have over five hundred divisors?'
import numpy

def nthTriangleNumber(n):
    number = int((n * (n + 1)) / 2)
    return(number)

def listDivisors(n):
    divisors = [1, n]
    for i in range(2, int(numpy.sqrt(n) + 1)):
        if n % i == 0:
            divisors.append(int(i))
            if int(i) != int(n/i):
                divisors.append(int(n/i))
    #divisors.sort()
    return(divisors)

def divisibleTriangleNumber(minExcl):
    n = 1
    found = False
    while found == False:
        tNumber = nthTriangleNumber(n)
        nDivisors = len(listDivisors(tNumber))
        if nDivisors > minExcl:
            found = True
            print('n = ' + str(n) + ', Triangle Number = ' + str(tNumber))
        else:
            n += 1

if __name__ == '__main__':
    #nthTriangleNumber(3)
    #listDivisors(64)
    divisibleTriangleNumber(500)