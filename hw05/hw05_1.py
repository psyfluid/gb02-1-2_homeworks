# задача 1. Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход
# друг после друга. Первый ход определяется жеребьёвкой. За один ход можно
# забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему
# последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все
# конфеты у своего конкурента?
# Делаем игру против бота

# а) Подумайте как наделить бота ""интеллектом""

import random


def input_selection(invite_text, selection_type):
    for _ in range(3):
        try:
            input_choice = int(input(invite_text))
            if 1 <= input_choice <= 2:
                return input_choice - 1
            else:
                print(f'Wrong {selection_type}. Try again.')
        except ValueError:
            print(f'Wrong {selection_type}. Try again.')
    return


def candy_game(candies, max_per_turn):

    two_players = input_selection('Select game mode (1 player - 1, 2 players - 2): ',
                                  selection_type='game mode')
    if two_players is None:
        print('Wrong game mode. Game over.')
        return

    if not two_players:
        hard_level = input_selection('Select difficulty level (easy - 1, hard - 2): ',
                                    selection_type='difficulty level')
        if hard_level is None:
            print('Wrong difficulty level. Game over.')
            return

    player_turn = random.choice([True, False])

    if two_players:
        player = '2' if player_turn else '1'
        print(f'Congratulations! Player {player} won the toss and is making his first move!')
    else:
        if player_turn:
            print('Congratulations! You have won the toss and you are making your first move!')
        else:
            print('As a result of the toss, the first move is mine.')

    while candies:
        print('Candies left:', candies)
        max_turn = min(max_per_turn, candies)
        if player_turn or two_players:
            for _ in range(3):
                try:
                    if two_players:
                        player = '2' if player_turn else '1'
                        invite_text = f'Player {player} turn (take from 1 to {max_turn} candies): '
                    else:
                        invite_text = f'Your turn (take from 1 to {max_turn} candies): '
                    turn = int(input(invite_text))
                    if 1 <= turn <= max_turn:
                        break
                    print('Try again!')
                except ValueError:
                    turn = 0
                    print('Try again!')

            if 1 <= turn <= max_turn:
                candies -= turn
            else:
                turn = 0
                break
        else:
            if hard_level:
                if candies <= max_turn:
                    turn = max_turn
                elif candies == max_turn + 1:
                    turn = 1
                else:
                    turn = candies % (max_per_turn + 1)
            else:
                turn = random.randint(1, max_turn)
            candies -= turn
            print('My turn:', turn)

        player_turn = not player_turn

    if turn:
        print('Candies left:', candies)
        if two_players:
            print(f'Player {"1" if player_turn else "2"} won!')
        else:
            print('You lose!' if player_turn else 'You win!')
        print('Game over')
    else:
        print('Wrong number of candies. Game over.')


def main():
    print('Welcome to the candy game!')
    try:
        candies = int(input('Input total number of candies: '))
        max_per_turn = int(input('Input maximum number of candies per turn: '))
    except ValueError as ex:
        print('Wrong number! Program terminated.')
        exit(ex)

    candy_game(candies, max_per_turn)


if __name__ == '__main__':
    main()
