# задача 2. Напишите программу для проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

def check_assertion(x, y, z):
    try:
        return (not (eval(str(x)) or eval(str(y)) or eval(str(z)))) == (
            not eval(str(x)) and not eval(str(y)) and not eval(str(z)))
    except Exception as ex:
        exit(ex)


def main():
    print(check_assertion(input('Input x: '), input('Input y: '), input('Input z: ')))


if __name__ == '__main__':
    main()
