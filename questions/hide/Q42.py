''''''

import numpy

scores = {
    'A': 1,
    'B': 2,
    'C': 3,
    'D': 4,
    'E': 5,
    'F': 6,
    'G': 7,
    'H': 8,
    'I': 9,
    'J': 10,
    'K': 11,
    'L': 12,
    'M': 13,
    'N': 14,
    'O': 15,
    'P': 16,
    'Q': 17,
    'R': 18,
    'S': 19,
    'T': 20,
    'U': 21,
    'V': 22,
    'W': 23,
    'X': 24,
    'Y': 25,
    'Z': 26
}

def scoreWord(word):
    score = 0
    for i in range(len(word)):
        score += scores[word[i]]
    return score

def generateTriangleNumbers(nTerms):
    triangleNumbers = []
    for n in range(1, nTerms + 1):
        triangleNumbers.append(int(n * (n + 1) / 2))
    return triangleNumbers

def triangleWordSearch(nTerms):
    words = numpy.loadtxt('words.txt', dtype='str', delimiter=',')
    triangleNumbers = generateTriangleNumbers(nTerms)
    triangleWords = 0
    for i in range(len(words)):
        if scoreWord(words[i].replace('"', '')) in triangleNumbers:
            triangleWords += 1
    print(triangleWords)

if __name__ == '__main__':
    #print(scoreWord('SKY'))
    #print(generateTriangleNumbers(10))
    triangleWordSearch(20)