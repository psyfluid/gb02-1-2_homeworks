# задача 4 необязательная Даны два многочлена. Задача - сформировать их сумму.

# например, 5*x^3 + 2*x^2 + 6 и 7*x^2+6*x+3 , Тогда их сумма будет равна
# 5*x^3 + 9*x^2 + 6*x + 9

import re
from math import fsum


def print_polynomial(parsed_eq, as_equation=False):
    terms = []

    for varexp, coeff in parsed_eq.items():
        if coeff:
            if abs(coeff) > 1 or not varexp[1]:
                term = f'{coeff}'
            else:
                term = '-' if coeff < 0 else ''

            if varexp[1]:
                term += '*' if abs(coeff) > 1 else ''
                term += f'{varexp[0]}^{varexp[1]}' if varexp[1] > 1 else varexp[0]

            terms.append(term)

    eq = ' + '.join(terms) + (' = 0' if as_equation else '')
    eq = eq.replace('+ -', '- ')
    return eq


def parse_polynomial(eq, real=False):
    eq = eq.replace(' ', '')
    eq = eq.replace('**', '^')
    coef1_pattern = '(?<![\*\d])([A-Za-z])'
    eq = re.sub(coef1_pattern, lambda m: '1*' + m.group(1), eq)
    exp1_pattern = '([A-Za-z])(?![\^\w])'
    eq = re.sub(exp1_pattern, lambda m: m.group(1) + '^1', eq)

    ex, *res = eq.split('=')

    terms_pattern = '(?:(\-?\d+\.?\d*)\*?)(\w*)(?:\^(\-?[\d\w]*\.?\d*))?'
    try:
        coefficients, variables, exponents \
            = zip(*re.findall(terms_pattern, ex))
        if res:
            res_coefficients, res_variables, res_exponents \
                = zip(*re.findall(terms_pattern, res))
    except ValueError:
        print('No variables found.')
        return None

    try:
        coefficients = list(map(float if real else int, coefficients))
        if res:
            res_coefficients = list(map(lambda x: -float(x) if real
                                        else -int(x), res_coefficients))
    except ValueError:
        print(f'Input only {"real" if real else "natural"} numbers as coefficients.')
        return None

    if res:
        coefficients += res_coefficients
        variables += res_variables
        exponents += res_exponents

    try:
        exponents = list(map(lambda x: int(x) if x else 0, exponents))
    except ValueError:
        print('Input only natural numbers as exponents.')
        return None

    f_sum = fsum if real else sum

    parsed = {(var, exp): f_sum([term[0] for term
              in zip(coefficients, variables, exponents)
              if term[1] == var and term[2] == exp])
              for var, exp in set(zip(variables, exponents))}

    return dict(sorted(parsed.items(),
                       key=lambda k: (k[0][0] if k[0][0] else '~', -k[0][1])))


def main():
    polynomial1 = input('Input first polynomial: ')
    polynomial2 = input('Input second polynomial: ')
    parsed_polynomial = parse_polynomial(polynomial1 + '+' + polynomial2)

    print('Sum of two polynomials:', print_polynomial(parsed_polynomial), sep='\n')


if __name__ == '__main__':
    main()
