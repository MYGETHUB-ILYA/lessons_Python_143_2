def is_year_leap(year):
    if year % 4 == 0:
        a = True
    else:
        a = False
    return a


test_year = 2024
print(f'Год {test_year}:', is_year_leap(test_year))
