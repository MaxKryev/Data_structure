from math import pi


# Task_1
a = float(input())


def get_perimetr(a: float) -> float:
    return 4 * a


result = get_perimetr(a)
print("Периметр квадрата =", result)


# Task_2
a = float(input())


def get_square(a: float) -> float:
    return a ** 2


result = get_square(a)
print("Площадь квадрата =", result)


# Task_3
a, b = float(input()), float(input())


def get_params(a: float, b: float) -> tuple[float, float]:
    S = a * b
    P = 2 * (a + b)
    return S, P


result = get_params(a, b)
print("Площадь прямоугольника =", result[0], "Периметр прямоугольника =", result[1])


# Task_4
d = float(input())


def get_circumference(d: float) -> float:
    return pi * d


result = get_circumference(d)
print("Длина окружности =", result)


# Task_5
a = float(input())


def get_params(a: float) -> tuple[float, float]:
    V = a ** 3
    S = 6 * (a ** 2)
    return V, S


result = get_params(a)
print("Обьем куба = ", result[0], "Площадь поверхности =", result[1])


# Task_6
a, b, c = float(input()), float(input()), float(input())


def get_params(a: float, b: float, c: float) -> tuple[float, float]:
    V = a * b * c
    S = 2 * (a * b + b * c + a * c)
    return V, S


result = get_params(a, b, c)
print("Объем паралелепипеда =", result[0], "Площадь поверхности =", result[1])


# Task_7
R = float(input())


def get_params(R: float) -> tuple[float, float]:
    L = 2 * pi * R
    S = pi * (R ** 2)
    return L, S


result = get_params(R)
print("Длина окружности =", result[0], "Площадь круга =", result[1])


# Task_8
a, b = float(input()), float(input())


def get_average(a: float, b: float) -> float:
    return (a + b) / 2


result = get_average(a, b)
print("Среднее арифметическое =", result)


# Task_9
a, b = float(input()), float(input())


def get_geo_mean(a: float, b:float) -> tuple[str, float] | str:
    if a >= 0 and b >= 0:
        geo_mean = (a * b) ** 0.5
        return f"{'Среднее геометрическое = ' + f'{geo_mean}'}"
    else:
        return "Данные не соотвествуют условиям задачи"


result = get_geo_mean(a, b)
print(result)


# Task_10
a, b = float(input()), float(input())


def get_params(a: float, b: float) -> str:
    if a == 0 or b == 0:
        return "Данные не соотвествуют условиям задачи"
    else:
        sum_square = (a * a) + (b * b)
        dif_square = (a * a) - (b * b)
        mult_square = (a * a) * (b * b)
        quo_squares = (a * a) / (b * b)
        return f"{'Сумма квадратов = ' + f'{sum_square}' + ' Разность квадратов = ' + f'{dif_square}' + ' Произведение квадратов = ' + f'{mult_square}' + ' Частное квадратов = ' + f'{quo_squares}'}"


result = get_params(a, b)
print(result)
