# Задача 1 Задайте список из нескольких чисел. Напишите программу, которая
# найдёт сумму элементов списка, стоящих на нечётной позиции.

# *Пример:*

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import choices


def find_sum_odd_indices(seq):
    sum = 0
    for i in range(1, len(seq), 2):
        sum += seq[i]

    return sum


def main():
    try:
        list_length = int(input('Input list length: '))
        max_number = int(input('Input maximum number: '))
    except ValueError as ex:
        print('Input natural numbers!')
        exit(ex)

    rand_list = choices(range(max_number + 1), k=list_length)
    print('Random int list:', rand_list, sep='\n')

    print(f'Sum of elements with odd indices is {find_sum_odd_indices(rand_list)}')


if __name__ == '__main__':
    main()
