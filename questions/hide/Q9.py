'There exists exactly one Pythagorean triplet for which a + b + c = 1000.'
'Find the product abc.'

def triplet(sumabc):
    for a in range(1, sumabc - 1):
        for b in range(1, sumabc - a):
            c = sumabc - a - b
            if (a ** 2 + b ** 2 == c ** 2):
                print(a, b, c)
                print(a * b * c)


if __name__ == '__main__':
    triplet(1000)