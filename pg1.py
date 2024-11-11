import calendar

def is_leap_year(year):
    return calendar.isleap(year)

year = int(input("Enter a year: "))
print(is_leap_year(year))
