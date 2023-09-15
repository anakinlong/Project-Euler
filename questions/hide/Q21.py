'''Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.
Evaluate the sum of all the amicable numbers under 10000.'''
import numpy

def d(n):
    total = 1
    for i in range(2, int(numpy.sqrt(n) + 1)):
        if n % i == 0:
            total += int(i)
            if int(i) != int(n/i):
                total += n / i
    return(int(total))

def sumAmicable(maxExcl):
    pairs = []
    total = 0
    for n in range(1, maxExcl):
        if d(d(n)) == n:
            if d(n) != n:
                total += n
                pairs.append(n)
    print(total, pairs)

def test(n):
    print(d(d(n)))

if __name__ == '__main__':
    #print(sumProperDivisors(220))
    sumAmicable(10000)
    #test(220)