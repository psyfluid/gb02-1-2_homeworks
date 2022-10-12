# Задача 1. Напишите программу, которая принимает на вход вещественное или
# целое число и показывает сумму его цифр. Через строку нельзя решать.

# *Пример:*

# - 6782 -> 23
# - 0,56 -> 11

def sum_of_digits(num):
    factor = 1
    while num * factor - int(num * factor) > 0:
        factor *= 10

    num = int(num * factor)
    sum = 0
    while num > 0:
        sum += num % 10
        num //= 10

    return sum


def main():
    try:
        a = float(input('Input number: '))
    except ValueError as ex:
        print('Input real number!')
        exit(ex)

    print(f'Sum of digits of number {a} is {sum_of_digits(a)}')


if __name__ == '__main__':
    main()
