# Задача 5 НЕОБЯЗАТЕЛЬНАЯ. Напишите программу для проверки истинности
# утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z . Но теперь количество предикатов
# не три, а генерируется случайным образом от 5 до 25, проверяем это
# утверждение 100 раз, с помощью модуля time выводим на экран сколько времени
# отработала программа.

import random
from time import perf_counter_ns


def check_assertion(predicates):
    result1 = predicates[0]
    result2 = not predicates[0]

    for i in range(1, len(predicates)):
        result1 |= predicates[i]
        result2 &= not predicates[i]

    return not result1 == result2


def main():
    try:
        n = int(input('Input number of tests: '))
    except ValueError as ex:
        print('Input natural number!')
        exit(ex)

    start_time = perf_counter_ns()

    for i in range(n):
        predicates = [random.choice([True, False]) for i in range(random.randrange(5, 26))]
        print(f'Test {i + 1}:')
        print(f'For predicates {predicates} the assertion is {check_assertion(predicates)}')

    end_time = perf_counter_ns()
    exec_time = end_time - start_time
    unit = 'ms' if exec_time >= 10**6 else 'ns'
    print(f'Execution time: {exec_time / 10**6 if unit == "ms" else exec_time:,g} {unit}')


if __name__ == '__main__':
    main()
