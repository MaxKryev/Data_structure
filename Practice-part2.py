from typing import Tuple


# Task_1

L = int(input())


def get_length(L: int) -> int:
    return L // 100


result = get_length(L)
print("Длина в метрах:", result)


#Task_2

M = int(input())


def get_mass(M: int) -> int:
    return M // 1000


result = get_mass(M)
print("Масса в тоннах:", result)


#Task_3

file_bytes = int(input())


def get_kilobyte(file_bytes: int) -> int:
    return file_bytes // 1024


result = get_kilobyte(file_bytes)
print("Количество килобайт:", result)


#Task_4

A, B = int(input()), int(input())


def get_B_in_A(A: int, B: int) -> str:
    if A > B:
        return f"{'Отрезков В в А: '+ f'{A // B}'}"
    else:
        return "Данные не соответствуют условиям задачи"


result = get_B_in_A(A, B)
print(result)


#Task_5

A, B = int(input()), int(input())


def remainder_A(A: int, B: int) -> str:
    if A > B:
        return f"{'Остаток длины А: '+ f'{A % B}'}"
    else:
        return "Данные не соответствуют условиям задачи"


result = remainder_A(A, B)
print(result)


#Task_6

number = int(input())


def get_nums(number: int) -> tuple[int, int] | str:
    if 10 <= number < 100:
        first_num = number // 10
        second_num = number % 10
        return f"{'Десятки:' + f'{first_num}' + ' Единицы:' + f'{second_num}'}"
    else:
        return "Число не соответствует условиям задачи"


result = get_nums(number)
print(result)


#Task_7

number = int(input())


def get_params(number: int) -> tuple[int, int]:
    first_num = number // 10
    second_num = number % 10
    return first_num + second_num, first_num * second_num


result = get_params(number)
print("Сумма цифр:", result[0], "Произведение цифр:", result[1])


#Task_8

number = int(input())


def get_change(number: int) -> int:
    first_num = number // 10
    second_num = number % 10
    return int(str(second_num)+str(first_num))


result = get_change(number)
print(result)


#Task_9

number = int(input())


def get_hundred(number: int) -> int:
    return number // 100


result = get_hundred(number)
print(result)


#Task_10

number = int(input())


def get_nums(number: int) -> tuple[int, int]:
    return number % 10, number // 10 % 10


result = get_nums(number)
print("Единицы:", result[0], "Десятки:", result[1])
