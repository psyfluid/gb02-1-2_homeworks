# Задача 4 НЕОБЯЗАТЕЛЬНАЯ. Напишите программу, которая принимает на вход N и
# координаты двух точек и находит расстояние между ними в N-мерном пространстве.

def get_coordinates_from_input(dim):
    coordinates = [0.] * dim

    for i in range(dim):
        try:
            coordinates[i] = float(input(f'Input coordinate {i + 1}: '))
        except ValueError as ex:
            print('Input real numbers as coordinates!')
            exit(ex)

    return coordinates


def find_distance(point1, point2):
    sum_of_squares = 0
    for i in range(len(point1)):
        sum_of_squares += (point1[i] - point2[i]) ** 2
    return sum_of_squares ** 0.5


def main():
    try:
        n = int(input('Input the number of space dimensions: '))
    except ValueError as ex:
        print('Input natural number!')
        exit(ex)

    print('Input point A coordinates:')
    a = get_coordinates_from_input(n)

    print('Input point B coordinates:')
    b = get_coordinates_from_input(n)

    print(f'Distance between A and B is {find_distance(a, b):g}')


if __name__ == '__main__':
    main()
