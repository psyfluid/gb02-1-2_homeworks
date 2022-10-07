# задача 1. Напишите программу, которая принимает на вход цифру, обозначающую
# день недели, и проверяет, является ли этот день выходным.

def check_holiday(weekday):
    try:
        weekday = int(weekday)
    except ValueError:
        print('Input correct weekday number (from 1 to 7)')
        return None

    if weekday < 1 or weekday > 7:
        print('Input correct weekday number (from 1 to 7)')
        return None

    return weekday == 6 or weekday == 7


def main():
    print("It's a holiday: ",
          check_holiday(input('Input weekday number (from 1 to 7): ')))


if __name__ == '__main__':
    main()
