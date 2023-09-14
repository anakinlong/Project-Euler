'If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.'
'Find the sum of all the multiples of 3 or 5 below 1000.'

def SumOfMultiples(inputs, minIncl, maxExcl):

        multiples = []
        for i in inputs:
            for j in range(minIncl, maxExcl):
                if (j % i == 0):
                    if j not in multiples:
                        multiples.append(j)
        
        print(sum(multiples))

if __name__ == '__main__':
        SumOfMultiples([3, 5], 1, 1000)