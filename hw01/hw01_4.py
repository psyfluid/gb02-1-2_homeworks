# задача 4 HARD необязательная Напишите простой калькулятор, который считывает
# с пользовательского ввода три строки: первое число, второе число и операцию,
# после чего применяет операцию к введённым числам ("первое число" "операция"
# "второе число") и выводит результат на экран.

# Поддерживаемые операции: +, -, /, *, mod, pow, div, где
# mod — это взятие остатка от деления,
# pow — возведение в степень,
# div — целочисленное деление.

# Если выполняется деление и второе число равно 0, необходимо выводить строку
# "Деление на 0!".

# Обратите внимание, что на вход программе приходят вещественные числа.

from decimal import Decimal


def input_for_calculate():
    try:
        a = Decimal(input('Input first number: '))
        b = Decimal(input('Input second number: '))
    except Exception as ex:
        print('Input only real numbers:')
        exit(ex)

    string_operator = input('Input operator: ').strip()

    return a, b, string_operator


def calculate(a, b, string_operator):
    if string_operator == '+':
        return a + b
    elif string_operator == '-':
        return a - b
    elif string_operator == '/':
        return a / b if b else 'Division by zero!'
    elif string_operator == '*':
        return a * b
    elif string_operator == 'mod':
        return a % b if b else 'Division by zero!'
    elif string_operator == 'pow':
        return a ** b
    elif string_operator == 'div':
        return a // b if b else 'Division by zero!'
    else:
        return 'Unknown operator!'


def main():
    print(calculate(*input_for_calculate()))


if __name__ == '__main__':
    main()
