''''''
import itertools

primes = [2, 3, 5, 7, 11, 13, 17]

def generatePandigitals(nDigits):
    number = ''
    for i in range(0, nDigits + 1):
        number += str(i)
    pandigitalArrays = list(itertools.permutations(list(number)))
    pandigitalList = []
    for pandigital in pandigitalArrays:
        digits = ''
        for digit in pandigital:
            digits += digit
        if digits[0] != '0':
            pandigitalList.append(int(digits))
    return(pandigitalList)

def thingy(n, firstDigit):
    number = ''
    for i in range(firstDigit, firstDigit + 3):
        number += str(n)[i]
    return int(number)

def search():
    total = 0
    pandigitalList = generatePandigitals(9)
    for n in pandigitalList:
        if all(thingy(n, i + 1) % primes[i] == 0 for i in range(0, 7)):
            total += n
    print(total)

if __name__ == '__main__':
    #print(generatePandigitals(9)[2])
    #print(thingy(1234567890, 2))
    search()