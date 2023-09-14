'''145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
Find the sum of all numbers which are equal to the sum of the factorial of their digits.
Note: As 1! = 1 and 2! = 2 are not sums they are not included.'''

# Since 9!x7 < 9999999, the numbers have at most 7 digits.

def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact

def digitFactorial(n):
    digits = str(n)
    total = 0
    for digit in digits:
        total += factorial(int(digit))
    return total

def curiousCheck(maxExcl):
    curious = []
    for n in range(1, maxExcl):
        if digitFactorial(n) == n:
            curious.append(n)
    print(curious)

if __name__ == '__main__':
    #print(digitFactorial(145))
    curiousCheck(10000000)