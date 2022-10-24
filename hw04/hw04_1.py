# задача 1. Задайте натуральное число N. Напишите программу, которая составит
# список простых множителей числа N.

def prime_factors(n):
    i = 2

    prime_factors_list = []
    while i <= n:
        if n % i == 0:
            prime_factors_list.append(i)
            n //= i
        else:
            i += 1

    return prime_factors_list


def main():
    try:
        n = int(input('Input N: '))
    except ValueError as ex:
        print('Input natural number!')
        exit(ex)

    print(f'Prime factors of {n}:\n', prime_factors(n))


if __name__ == '__main__':
    main()
