'''An irrational decimal fraction is created by concatenating the positive integers:
0.123456789101112131415161718192021...
It can be seen that the 12th digit of the fractional part is 1.
If dn represents the nth digit of the fractional part, find the value of the following expression.
d1 x d10 x d100 x d1000 x d10000 x d100000 x d1000000'''

# 9 1-digits, 90 2-digits, 900 3-digits, 9*10^(n-1) n-digits.
# Could solve it with maths easily.

def fractionGenerator(l):
    number = ''
    i = 1
    while len(number) < l + 1:
        number += str(i)
        i += 1
    print(int(number[0]) * int(number[9]) * int(number[99]) * int(number[999]) * int(number[9999]) * int(number[99999]) * int(number[999999]))

if __name__ == '__main__':
    fractionGenerator(1000000)