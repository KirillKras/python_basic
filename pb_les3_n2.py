# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    list_len = len(origin_list)
    for i in range(list_len-1):
        for j in range(list_len-i-1):
            if origin_list[j] > origin_list[j+1]:
                origin_list[j], origin_list[j+1] = origin_list[j+1], origin_list[j]

    print(origin_list)


sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])