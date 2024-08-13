"""Бинарный метод поиска"""


def is_some_city(some_cities, candidate):
    # индекс первого элемента области поиска
    first = 0
    # индекс последнего элемента области поиска
    last = len(some_cities) - 1

    while (first <= last):
        # индекс среднего элемента области поиска
        middle = (first + last) // 2

        if candidate == some_cities[middle]:
            # если нашли слово-кандидат, поиск завершается удачно
            return True

        if candidate < some_cities[middle]:
            # если кандидат меньше, отбрасываем правую половину
            last = middle - 1
        else:
            # если кандидат больше, отбрасываем левую половину
            first = middle + 1

    return False


"""Пузырьковая сортировка"""


def bubble_sort(nums):
    # Мы устанавливаем swapped == True чтобы цикл выполнился хотя бы раз
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                # Меняем элементы
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Устанавливаем флаг == True, чтобы цикл повторился
                swapped = True


# Проверяем работу
random_list_of_nums = [5, 2, 1, 8, 4]
bubble_sort(random_list_of_nums)
print(random_list_of_nums)

# Output: [1, 2, 4, 5, 8]