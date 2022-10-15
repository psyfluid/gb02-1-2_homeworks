# Задача 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# *Пример:*

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from random import choices


def get_pair_products(seq):
    products = []
    for i in range((len(seq) + 1) // 2):
        products.append(seq[i] * seq[-i - 1])

    return products


def main():
    try:
        list_length = int(input('Input list length: '))
        max_number = int(input('Input maximum number: '))
    except ValueError as ex:
        print('Input natural numbers!')
        exit(ex)

    rand_list = choices(range(max_number + 1), k=list_length)
    print('Random int list:', rand_list, sep='\n')

    print('Pair products:', get_pair_products(rand_list), sep='\n')


if __name__ == '__main__':
    main()
