'''Find the sum of the digits in the number 100!'''

def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact

def sumOfDigits(n):
    digits = str(n)
    total = 0
    for i in range(len(digits)):
        total += int(digits[i])
    print('Sum of digits = ' + str(total))

if __name__ == '__main__':
    sumOfDigits(factorial(100))