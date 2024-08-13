#Task_1

A = int(input())


def get_truth(A: int) -> bool:
    return A is A > 0


result = get_truth(A)
print(result)


#Task_2

A = int(input())


def get_truth(A: int) -> bool:
    return A % 2 != 0


result = get_truth(A)
print(result)

#Task_3

A = int(input())


def get_truth(A: int) -> bool:
    return A % 2 == 0


result = get_truth(A)
print(result)


#Task_4

A, B = int(input()), int(input())


def get_truth(A: int, B: int) -> bool:
    return A > 2 and B <= 3


result = get_truth(A, B)
print(result)


#Task_5

A, B = int(input()), int(input())


def get_truth(A: int, B: int) -> bool:
    return A >= 0 or B < -2


result = get_truth(A, B)
print(result)


#Task_6

A, B, C = int(input()), int(input()), int(input())


def get_truth(A: int, B: int, C: int) -> bool:
    return A < B < C


result = get_truth(A, B, C)
print(result)


#Task_7

A, B, C = int(input()), int(input()), int(input())


def get_truth(A: int, B: int, C: int) -> bool:
    return A < B < C or A > B > C


result = get_truth(A, B, C)
print(result)


#Task_8

A, B = int(input()), int(input())


def get_truth(A: int, B: int) -> bool:
    return A % 2 != 0 and B % 2 != 0


result = get_truth(A, B)
print(result)


#Task_9

A, B = int(input()), int(input())


def get_truth(A: int, B: int) -> bool:
    return A % 2 != 0 or B % 2 != 0


result = get_truth(A, B)
print(result)


#Task_10

A, B = int(input()), int(input())


def get_truth(A: int, B: int) -> bool:
    cond = 0
    if A % 2 != 0:
        cond += 1
    if B % 2 != 0:
        cond += 1
    return cond == 1


result = get_truth(A, B)
print(result)