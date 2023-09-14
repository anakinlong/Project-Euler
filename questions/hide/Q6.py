'Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.'

def difference(numbers):
    sumOfSquares = 0
    for i in numbers:
        sumOfSquares += (i ** 2)

    squareOfSum = sum(numbers) ** 2

    difference = squareOfSum - sumOfSquares

    print(difference)

if __name__ == '__main__':
    difference(range(1,101))