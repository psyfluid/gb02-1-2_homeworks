# задача5 HARD необязательная.
# Сгенерировать массив случайных целых чисел размерностью m*n (размерность
# вводим с клавиатуры) , причем чтоб количество элементов было четное. Вывести
# на экран красивенько таблицей. Перемешать случайным образом элементы массива,
# причем чтобы каждый гарантированно переместился на другое место и выполнить
# это за m*n / 2 итераций. То есть если массив три на четыре, то надо выполнить
# не более 6 итераций. И далее в конце опять вывести на экран как таблицу.

import random


def shuffle_matrix(list_2d):
    cols = len(list_2d[0])

    indices = list(range(len(list_2d) * cols))

    while len(indices) > 1:
        i = random.choice(indices)
        indices.remove(i)
        j = random.choice(indices)
        indices.remove(j)

        list_2d[i // cols][i % cols], list_2d[j // cols][j % cols] \
            = list_2d[j // cols][j % cols], list_2d[i // cols][i % cols]


def main():
    try:
        m = int(input('Input number of rows: '))
        n = int(input('Input number of columns: '))
        if m * n % 2:
            print('Please input at least one even size!')
            exit()
        max_number = int(input('Input maximum number: '))
    except ValueError as ex:
        print('Input natural numbers!')
        exit(ex)
    print()

    matrix = [[random.randrange(max_number) for _ in range(n)] for _ in range(m)]
    print('Original matrix:', *matrix, sep='\n')
    print()

    shuffle_matrix(matrix)
    print('Shuffled matrix', *matrix, sep='\n')
    print()


if __name__ == '__main__':
    main()
