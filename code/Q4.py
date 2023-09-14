'A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.'
'Find the largest palindrome made from the product of two 3-digit numbers.'

def palindromes(minIncl, maxExcl):
    palindromes = []
    for i in range(minIncl, maxExcl):
        for j in range(minIncl, maxExcl):
            value = i * j
            if (str(value) == str(value)[::-1]):
                palindromes.append(value)
    print(palindromes)
    print(max(palindromes))

if __name__ == '__main__':
    palindromes(100, 1000)