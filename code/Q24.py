'''A permutation is an ordered arrangement of objects.
If all of the permutations are listed numerically or alphabetically, we call it lexicographic order.
What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?'''
import itertools

def permutations(digits):
    return list(itertools.permutations(digits))

if __name__ == '__main__':
    print(permutations(range(10))[10 ** 6 - 1])