"""
You are given the following information, but you may prefer to do some research for yourself.

- 1 Jan 1900 was a Monday.
- Thirty days has September, April, June and November. All the rest have thirty-one, saving February alone, which has
twenty-eight, rain or shine. and on leap years, twenty-nine.
- A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

try:
    import lib
except ModuleNotFoundError:
    from questions import lib


ANSWER = 171


# A dictionary mapping each day to its day-of-week value that is used below:
DAYS = {
    "MON": 1,
    "TUE": 2,
    "WED": 3,
    "THU": 4,
    "FRI": 5,
    "SAT": 6,
    "SUN": 7,
}


# A dictionary mapping each month to how many days it ordinarily has:
MONTHS = {
    "JAN": 31,
    "FEB": 28,
    "MAR": 31,
    "APR": 30,
    "MAY": 31,
    "JUN": 30,
    "JUL": 31,
    "AUG": 31,
    "SEP": 30,
    "OCT": 31,
    "NOV": 30,
    "DEC": 31,
}


def is_leap(year: int) -> bool:
    """
    Decide whether a particular year is a leap year or not.

    :param year: the year (Julian)>

    :return: True if a leap year, otherwise False.
    """
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    return False


@lib.profiling.profileit()
def counting_sundays(start_day: str, start_year: int, end_year: int):
    """
    Count how many Sundays fell on the first of the month during a period of years.

    :param start_day: which day of the week the start day was.
    :param start_year: the first year of the period.
    :param end_year: the final year of the period.

    :return: how many Sundays fell on the first of the month.
    """
    # Starting from our start day, we keep track of the day of week value:
    day = DAYS[start_day]

    # Loop through each year and month in order:
    sunday_count = 0
    for year in range(start_year, end_year + 1):
        for month, days in MONTHS.items():
            # Add the correct number of days to the counter so that we are now at the first of the month:
            day += days
            # Add an extra day in February if it is a leap year:
            if is_leap(year) and month == "FEB":
                day += 1

            # Check if this day is Sunday by checking its value mod 7:
            if day % 7 == 0:
                sunday_count += 1

        # Reset the day of week value to just its value mod 7 each year to prevent it from getting too large:
        day = day % 7

    return sunday_count


if __name__ == '__main__':

    answer = counting_sundays("TUE", 1901, 2000)
