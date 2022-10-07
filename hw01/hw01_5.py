# Задача 5 VERY HARD SORT необязательная
# Задайте двумерный массив из целых чисел. Количество строк и столбцов задается
# с клавиатуры. Отсортировать элементы по возрастанию слева направо и сверху вниз.
# Например, задан массив:
# 1 4 7 2
# 5 9 10 3

# После сортировки
# 1 2 3 4
# 5 7 9 10

def quicksort(items):
    if len(items) <= 1:
        return items
    else:
        pivot = items[0]
        lesser = quicksort([x for x in items[1:] if x < pivot])
        greater = quicksort([x for x in items[1:] if x >= pivot])
        return lesser + [pivot] + greater


def quicksort_2d_inplace(items_2d):
    sorted_items = quicksort([x for row in items_2d for x in row])
    rows = len(items_2d)
    columns = len(items_2d[0])
    for i in range(rows):
        for j in range(columns):
            items_2d[i][j] = sorted_items[i * columns + j]


def quicksort_2d(items_2d):
    sorted_items = quicksort([x for row in items_2d for x in row])
    rows = len(items_2d)
    columns = len(items_2d[0])
    return [[sorted_items[i * columns + j]
            for j in range(columns)] for i in range(rows)]


def int_array_from_input():
    try:
        rows = int(input('Input number of rows: '))
        columns = int(input('Input number of columns: '))
        print()
        new_array = [[int(input(f'Input element [{i}][{j}]: '))
                     for j in range(columns)] for i in range(rows)]
        print()
        return new_array

    except ValueError as ex:
        print('Input only integer numbers:')
        exit(ex)


def main():
    numbers = int_array_from_input()

    print('Input array: \n', numbers, '\n')

    print('Sorted array: \n', quicksort_2d(numbers), '\n')
    print('Original array: \n', numbers, '\n')

    quicksort_2d_inplace(numbers)
    print('Sorted original array: \n', numbers)


if __name__ == '__main__':
    main()
