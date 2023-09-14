'The prime factors of 13195 are 5, 7, 13 and 29.'
'What is the largest prime factor of the number 600851475143 ?'
import numpy

def primeFactors(number):
    i = 2
    factors = []
    while i <= numpy.sqrt(number):
        if (number % i):
            i = i + 1
        else:
            number = number / i
            factors.append(i)
    if number > 1:
        factors.append(number)
    print(factors)

if __name__ == '__main__':
    primeFactors(600851475143)