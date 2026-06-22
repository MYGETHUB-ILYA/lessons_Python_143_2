def month_to_season(month):
    if month <= 0 or month >= 13:
        print("Такого месяца нет. Введите от 1 до 12")
    elif month <= 1 or month < 3 or month == 12:
        print("Зима")
    elif month <= 3 or month < 6:
        print("Весна")
    elif month <= 7 or month < 9:
        print("Лето")
    else:
        print("Осень")


for i in range(1, 13):
    month_to_season(i)
