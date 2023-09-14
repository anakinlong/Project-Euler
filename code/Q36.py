'''Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.'''

def isPalindrome(n):
    digits = str(n)
    palindrome = True
    for i in range(len(digits)):
        if digits[i] != digits[-i-1]:
            palindrome = False
    return palindrome

def palindromeSearch(maxExcl):
    total = 0
    for n in range(1, maxExcl):
        if isPalindrome(n) == True:
            binaryn = int(bin(n).replace('0b', ''))
            if isPalindrome(binaryn) == True:
                total += n
    print(total)

if __name__ == '__main__':
    #print(isPalindrome(56788765))
    palindromeSearch(1000000)