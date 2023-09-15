'What is the sum of the digits of the number 2^1000?'

def sumOfDigits(n):
    digits = str(n)
    total = 0
    for i in range(len(digits)):
        total += int(digits[i])
    print('n = ' + str(digits) + ', sum of digits = ' + str(total))

if __name__ == '__main__':
    sumOfDigits(2 ** 1000)