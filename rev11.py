def leap_year(year):
    if year % 4 == 0:
        return True
    elif year % 100 == 0 and year % 400 == 0:
        return True
    else:
        return False

year = int(input("Enter a year: "))

if leap_year(year):
    print(f"{year} is a leap year")
else:
    print(f"{year} is NOT a leap year")

