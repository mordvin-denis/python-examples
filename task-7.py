# 7. Сравнить 2 списка чисел, содержат ли они только одинаковые элементы.
# Пример. [1, 8, 4] по этой задаче равно [4, 1, 4, 8, 1]

if __name__ == '__main__':
    list1 = [1, 8, 4, 3] # [1, 8, 4]
    list2 = [4, 1, 4, 8, 1] # [4, 1, 8]

    uniq_list1 = []
    uniq_list2 = []

    result = True

    for value in list1:
        if value not in uniq_list1:
            uniq_list1.append(value)

    for value in list2:
        if value not in uniq_list2:
            uniq_list2.append(value)

    if len(uniq_list1) != len(uniq_list2):
        result = False
    else:
        for value in uniq_list1:
            if value not in uniq_list2:
                result = False
                break

    print(result)
