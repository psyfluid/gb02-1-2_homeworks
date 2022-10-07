# задача 3. Напишите программу, которая принимает на вход координаты точки
# (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой
# находится эта точка (или на какой оси она находится).

def find_quadrant(x, y):
    if x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    elif x > 0 and y < 0:
        return 4
    elif x == 0 and y:
        return 'y'
    else:
        return 'x'


def main():
    try:
        x = float(input('Input x coordinate: '))
        y = float(input('Input y coordinate: '))
    except ValueError as ex:
        print('Input only real numbers:')
        exit(ex)

    quadrant = find_quadrant(x, y)

    if isinstance(quadrant, int):
        print(f'The quadrant number is {quadrant}')
    else:
        print(f'The point is on the {quadrant} axis')


if __name__ == '__main__':
    main()
