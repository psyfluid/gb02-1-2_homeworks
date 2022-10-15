# Задача 4. Напишите программу, которая будет преобразовывать десятичное число
# в двоичное. Нельзя использовать готовые функции.

# *Пример:*

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def convert_to_binary(num):
    return '-' + convert_to_binary_rec(-num) if num < 0 \
        else '' + convert_to_binary_rec(num)


def convert_to_binary_rec(num):
    return convert_to_binary_rec(num // 2) + str(num % 2) if num else ''


def main():
    try:
        n = int(input('Input number: '))
    except ValueError as ex:
        print('Input natural number!')
        exit(ex)

    print(f'Number {n} in binary form is {convert_to_binary(n)}')


if __name__ == '__main__':
    main()
