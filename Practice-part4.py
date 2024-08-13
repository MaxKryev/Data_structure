#Task_1

lst = [1, 2, 3, 4, 5]


def get_nums(lst: list) -> tuple[int, int, list]:
    return lst[0], lst[2], lst[:3]


result = get_nums(lst)
print(*result, sep=", ")


#Task_2

lst = ["Ростов", "+", "на", "-", "Дону"]
lst[1] = lst[3]
print(lst[0], lst[1], lst[2], lst[3], lst[4], sep="")


#Task_3

lst_1 = ["a", "s", "1", "a", "32", "23"]
lst_2 = sorted(lst_1)[:3]
lst_1 = sorted(lst_1)[3:]
print(lst_1, lst_2)


#Task_3

lst_1 = ["a", "s", "a"]
lst_1.pop()
lst_1 = lst_1[::-1]
print(lst_1)

#Task_4

lst = ["a", "s", "1", "a", "32", "23"]
lst = set(lst)
print(lst)
"""Остались только уникальные элементы списка"""


