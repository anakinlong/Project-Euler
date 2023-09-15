'''The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it 
may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.
We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
There are exactly four non-trivial examples of this type of fraction, less than one in value, 
and containing two digits in the numerator and denominator.
If the product of these four fractions is given in its lowest common terms, find the value of the denominator.'''

def fraction_checker(num, denom):
    correct = num / denom
    for i in range(len(str(num))):
        for j in range(len(str(denom))):
            if str(num)[i] == str(denom)[j]:
                #print(str(num)[i], str(denom)[j])
                if not(str(num)[i] == '0' and (i == len(str(num)) - 1 or j == len(str(denom)) - 1)):
                    new_num = int(str(num)[:i] + str(num)[i+1:])
                    new_denom = int(str(denom)[:j] + str(denom)[j+1:])
                    if new_denom != 0:
                        if new_num / new_denom == correct:
                            return True
    return False


def fraction_finder(min_incl, max_excl):
    fractions = []
    for numerator in range(min_incl, max_excl):
        for denominator in range(numerator + 1, max_excl):
            if fraction_checker(numerator, denominator) == True:
                fractions.append(str(numerator) + '/' + str(denominator))
    print(fractions)

if __name__ == '__main__':
    #print(fraction_checker(46, 98))
    fraction_finder(10, 1000)