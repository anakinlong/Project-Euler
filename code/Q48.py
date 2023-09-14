'''The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.'''

def last_n_digits(number, n_digits):
    result = 1
    for i in range(number):
        result *= number
        if len(str(result)) > n_digits:
            result = int(str(result)[-n_digits:])
    return result

def adding(min_incl, max_incl, n_digits):
    total = 0
    for number in range(min_incl, max_incl + 1):
        total += last_n_digits(number, n_digits)
        if len(str(total)) > n_digits:
            total = int(str(total)[-n_digits:])
    print(total)

if __name__ == '__main__':
    #print(11 ** 11)
    #print(last_n_digits(11, 10))
    adding(1, 1000, 10)