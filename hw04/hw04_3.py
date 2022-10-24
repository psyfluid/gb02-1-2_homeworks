# задача 3. Задана натуральная степень k. Сформировать случайным образом список
# коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен
# степени k.

# *Пример:*

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import choices


def generate_equation(k, min_coef, max_coef):
    coefficients = choices(range(min_coef, max_coef+1), k=k+1)
    terms = []

    for idx, coeff in enumerate(coefficients):
        if coeff:
            exponent = k - idx
            term = f'{coeff}' if abs(coeff) > 1 or not exponent else ''

            if exponent:
                term += '*' if abs(coeff) > 1 else ''
                term += f'x^{exponent}' if exponent > 1 else 'x'

            terms.append(term)

    eq = ' + '.join(terms) + ' = 0'
    eq = eq.replace('+ -', '- ')
    return eq


def main():
    try:
        k = int(input('Input exponent k: '))
        min_coef = int(input('Input minimum coefficient: '))
        max_coef = int(input('Input maximum coefficient: '))
    except ValueError as ex:
        print('Input natural number!')
        exit(ex)

    file_name = 'equation.txt'
    with open(file_name, 'w') as f:
        res = generate_equation(k, min_coef, max_coef)
        f.write(res)
        print(f'Generated polynomial with exponent {k}:\n{res}')
        print(f'The result was written to the file "{file_name}".')


if __name__ == '__main__':
    main()
