def is_leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    return year % 4 == 0

def days_in_month(year, month):
    month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2 and is_leap_year(year):
        return 29
    return month_days[month]

def weekday_monday_zero(year, month, day):
    # 1900-01-01 is Monday -> 0
    days = 0
    for y in range(1900, year):
        days += 366 if is_leap_year(y) else 365
    for m in range(1, month):
        days += days_in_month(year, m)
    days += day - 1
    return days % 7

def solve(start_year=1901, end_year=2000):
    count = 0
    for year in range(start_year, end_year + 1):
        for month in range(1, 13):
            if weekday_monday_zero(year, month, 1) == 6:  # Sunday
                count += 1
    return count

if __name__ == "__main__":
    assert weekday_monday_zero(1900, 1, 1) == 0, "Checkpoint failed for 1900-01-01"
    assert solve(1901, 1901) == 2, "Checkpoint failed for year 1901"
    print(solve())
