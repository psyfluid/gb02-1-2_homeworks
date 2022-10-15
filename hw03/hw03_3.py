# Задача 3. Задайте список из вещественных чисел. Напишите программу, которая
# найдёт разницу между максимальным и минимальным значением дробной части
# элементов.

# *Пример:*

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

from random import choices


def find_decimal_difference(seq, prec=2):

    min_dec = max_dec = 0

    for i in range(len(seq)):
        decimal_part = seq[i] - int(seq[i])
        if decimal_part:
            if min_dec == 0 or decimal_part < min_dec:
                min_dec = decimal_part

            if decimal_part > max_dec:
                max_dec = decimal_part

    return round(max_dec - min_dec, prec)


def main():
    try:
        list_length = int(input('Input list length: '))
        max_number = int(input('Input maximum number: '))
        precision = int(input('Input decimal precision: '))
    except ValueError as ex:
        print('Input natural numbers!')
        exit(ex)

    rand_list = choices([x / 10 ** precision
                        for x in range(max_number * 10 ** precision)],
                        k=list_length)

    print('Random float list:', rand_list, sep='\n')

    print('The difference between the minimum and maximum decimal part is',
          find_decimal_difference(rand_list, precision))


if __name__ == '__main__':
    main()
