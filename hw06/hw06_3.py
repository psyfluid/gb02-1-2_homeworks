# Задача FOOTBALL необязательная: Напишите программу, которая принимает на
# стандартный вход список игр футбольных команд с результатом матча и выводит
# на стандартный вывод сводную таблицу результатов всех матчей.
#
# За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.
#
# Формат ввода следующий:
# В первой строке указано целое число nn — количество завершенных игр.
# После этого идет nn строк, в которых записаны результаты игры в следующем
# формате:
# Перваякоманда;Забитопервойкомандой;Втораякоманда;Забитовторойкомандой
#
# Вывод программы необходимо оформить следующим образом:
# Команда:Всегоигр Побед Ничьих Поражений Всегоочков
#
# Конкретный пример ввода-вывода приведён ниже.
#
# Порядок вывода команд произвольный.
#
# Sample Input:
#
# 3
# Спартак;9;Зенит;10
# Локомотив;12;Зенит;3
# Спартак;8;Локомотив;15
# Sample Output:
#
# Спартак:2 0 0 2 0
# Зенит:2 1 0 1 3
# Локомотив:2 2 0 0 6


def get_data():
    try:
        n = int(input('Введите количество игр: '))
    except ValueError as e:
        exit(e)

    return [input(f'Игра {i}: ') for i in range(1, n + 1)]


def get_results(games):
    results = {}
    for game in games:
        team1, score1, team2, score2 = game.strip().split(';')
        team1_results = results.get(team1, [0, 0, 0, 0, 0])
        team2_results = results.get(team2, [0, 0, 0, 0, 0])
        team1_results[0] += 1
        team2_results[0] += 1

        try:
            if score1 == score2:
                team1_results[2] += 1
                team2_results[2] += 1
                team1_results[4] += 1
                team2_results[4] += 1
            elif int(score1) > int(score2):
                team1_results[1] += 1
                team2_results[3] += 1
                team1_results[4] += 3
            else:
                team2_results[1] += 1
                team1_results[3] += 1
                team2_results[4] += 3
        except ValueError as e:
            exit(e)

        results[team1] = team1_results
        results[team2] = team2_results

    return dict(sorted(results.items()))


def print_results(results):
    for k, v in results.items():
        print(f'{k}:', *v)


def main():
    games = get_data()
    print_results(get_results(games))


if __name__ == '__main__':
    main()
