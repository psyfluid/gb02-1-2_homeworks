# задача 4 необязательная. Найдите корни квадратного уравнения, уравнение
# вводит через строку пользователь. например, 6*x^2+5*x+6=0 . Само собой,
# уравнение может и не иметь решения. Предусмотреть все варианты, сделать
# обработку исключений.

import re
from math import fsum


def parse_equation(eq):
    eq = eq.replace(' ', '')
    eq = eq.replace('**', '^')
    eq = re.sub('(?<![\*\d])x', '1*x', eq)
    eq = re.sub('x(?![\^\w])', 'x^1', eq)

    try:
        ex, res = eq.split('=')
    except ValueError:
        print('Input an equation.',
              'Equal sign not found or more than one equal sign.')
        return None

    terms_pattern = '(?:(\-?\d+\.?\d*)\*?)(\w*)(?:\^(\-?[\d\w]*\.?\d*))?'
    try:
        coefficients, variables, exponents \
            = zip(*re.findall(terms_pattern, ex))
        res_coefficients, res_variables, res_exponents \
            = zip(*re.findall(terms_pattern, res))
    except ValueError:
        print('No variables found.')
        return None

    try:
        coefficients = list(map(float, coefficients))
        res_coefficients = list(map(lambda x: -float(x), res_coefficients))
    except ValueError:
        print('Input only real numbers as coefficients.')
        return None

    coefficients += res_coefficients
    variables += res_variables
    exponents += res_exponents

    variables = set(variables)
    if len(variables) > 2 if '' in variables else len(variables) > 1:
        print('Input an equation with one unknown.')
        return None

    return {exponent: fsum([term[1] for term in zip(exponents, coefficients)
            if term[0] == exponent]) for exponent in set(exponents)}


def parse_quadratic_equation(eq):
    terms = parse_equation(eq)
    if not terms:
        exit()

    a = b = c = 0
    for k, v in terms.items():
        if k == '2':
            a = v
        elif k == '1':
            b = v
        elif not k:
            c = v
        else:
            print('Input only quadratic equations.',
                  'The exponents must be between 0 and 2.')
            exit()

    return a, b, c


def find_roots(a, b, c):
    x_list = []
    d = b ** 2 - 4 * a * c
    if not a:
        x_list.append(0) if not c else x_list.append(-c / b) if b else None
    elif d > 0:
        x_list.append((-b - d ** 0.5) / (2 * a))
        x_list.append((-b + d ** 0.5) / (2 * a))
    elif d == 0:
        x_list.append(-b / (2 * a))

    return x_list


def solve_quadratic_equation(a, b, c):
    roots = find_roots(a, b, c)
    if len(roots) > 1:
        print(f'x1 = {roots[0]}, x2 = {roots[1]}')
    elif roots:
        print(f'x = {roots[0]}')
    else:
        print("The equation has no solution.")


def solve_quadratic_equation_from_string(eq):
    return solve_quadratic_equation(*parse_quadratic_equation(eq))


def main():
    equation = input('Input a quadratic equation: ')
    solve_quadratic_equation_from_string(equation)


if __name__ == '__main__':
    main()
