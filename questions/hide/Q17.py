'If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?'

ones = {
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine'
}

tens = {
    '10': 'ten',
    '11': 'eleven',
    '12': 'twelve',
    '13': 'thirteen',
    '14': 'fourteen',
    '15': 'fifteen',
    '16': 'sixteen',
    '17': 'seventeen',
    '18': 'eighteen',
    '19': 'nineteen'
}

others = {
    '2': 'twenty',
    '3': 'thirty',
    '4': 'forty',
    '5': 'fifty',
    '6': 'sixty',
    '7': 'seventy',
    '8': 'eighty',
    '9': 'ninety'
}

def number_to_words(n):
    n_with_leading_zeros = str(n).zfill(3)
    words = ''
    if n_with_leading_zeros[0] != '0':
        words += ones[n_with_leading_zeros[0]] + ' hundred'
        if n_with_leading_zeros[1:] != '00':
            words += ' and '
    if n_with_leading_zeros[1] != '0':
        if n_with_leading_zeros[1] == '1':
            words += tens[n_with_leading_zeros[1:]]
        else:
            words += others[n_with_leading_zeros[1]]
            if n_with_leading_zeros[2] != '0':
                words += ' ' + ones[n_with_leading_zeros[2]]
    else:
        if n_with_leading_zeros[2] != '0':
                words += ' ' + ones[n_with_leading_zeros[2]]
    return words

def letter_count():
    total_letters = len('one thousand'.replace(' ', ''))
    for n in range(1, 1000):
        total_letters += len(number_to_words(n).replace(' ', ''))
    return total_letters

if __name__ == '__main__':
    #print(number_to_words(999))
    print(letter_count())