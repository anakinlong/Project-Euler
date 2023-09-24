'''If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, 
there are exactly three solutions for p = 120:
{20,48,52}, {24,45,51}, {30,40,50}.
For which value of p ≤ 1000, is the number of solutions maximised?'''

def triangleSearch(maxIncl):
    mostSolutions = 0
    bestp = 0
    for p in range(3, maxIncl + 1):
        solutions = 0
        for a in range(1, int(p / 3) + 1):
            for b in range(a, int(2 * p / 3) + 1):
                c = p - a - b
                if (a ** 2 + b ** 2 == c ** 2):
                    solutions += 1
        if solutions > mostSolutions:
            bestp = p
            mostSolutions = solutions
    return bestp

if __name__ == '__main__':
    print(triangleSearch(1000))