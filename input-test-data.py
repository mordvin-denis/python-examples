
if __name__ == '__main__':
    # Способ задать начальный список №1
    test_list = [2, 5, 1, 8, 4, 2, 8]
    # Этот способ ближе к тестированию.
    # Он позволяет экономить время на вводе данных при разработке кода

    # Способ 2. Ввод с клавиатуры последовательности числел и преобразование их список чисел

    raw_string = input("Please input numbers separated by commas: ")

    raw_list = raw_string.split(',')

    result_list = []
    for item in raw_list:
        prepared_item = int(item.strip())
        result_list.append(prepared_item)


    print(result_list)


