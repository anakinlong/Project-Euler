'''How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?'''

months = [
    31,
    28,
    31,
    30,
    31,
    30,
    31,
    31,
    30,
    31,
    30,
    31
]

def counting_sundays():
    # Jan 1st 1901 was a Tuesday:
    day = 2
    
    sunday_count = 0
    for year in range(1901, 2001):
        for m in months:
            day += m
            if year % 4 == 0 and m == 28:
                day += 1
            if day % 7 == 0:
                sunday_count += 1
    print(sunday_count)

if __name__ == '__main__':
    counting_sundays()