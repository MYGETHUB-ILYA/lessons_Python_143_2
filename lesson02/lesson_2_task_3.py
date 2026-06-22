import math


def square(a):
    if a < 0:
        print('меньше нуля')
    else:
        square_numb = a*a
        return print(math.ceil(square_numb))


square(4)
square(3.7)
square(-3)
