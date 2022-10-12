# Задача 2. Напишите программу, которая принимает на вход число N и выдает
# набор произведений чисел от 1 до N.

# *Пример:*

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def factorial_list(num):
    product = 1
    products = []
    for i in range(1, num + 1):
        product *= i
        products.append(product)

    return products


def main():
    try:
        n = int(input('Input N: '))
    except ValueError as ex:
        print('Input natural number!')
        exit(ex)

    print(f'Factorial numbers from 1 to {n}:', factorial_list(n), sep='\n')


if __name__ == '__main__':
    main()
