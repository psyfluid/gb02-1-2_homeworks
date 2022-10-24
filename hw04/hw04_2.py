# задача 2 . Задайте последовательность чисел. Напишите программу, которая
# выведет список неповторяющихся элементов исходной последовательности.

from random import choices


def generate_numbers_list(size, min_number=0, max_number=9):
    num_list = choices(range(min_number, max_number + 1), k=size)
    return num_list, set(num_list)


def main():
    try:
        n = int(input('Input the size of the list of numbers: '))
        min_num = int(input('Input the minimum number in the list: '))
        max_num = int(input('Input the maximum number in the list: '))
    except ValueError as ex:
        print('Input natural number!')
        exit(ex)

    rand_list, unique_numbers = generate_numbers_list(n, min_num, max_num)
    print('Random list of numbers:\n', rand_list)
    print('Unique numbers in the list:\n', unique_numbers)


if __name__ == '__main__':
    main()
