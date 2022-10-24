import random
import json
import re
from datetime import datetime

# https://github.com/cinemagoer/cinemagoer
# pip install cinemagoer
from imdb import Cinemagoer, IMDbError

IA = Cinemagoer()
FILMS = {}
FILE_NAME = 'films.json'


def save():
    global FILMS
    FILMS = dict(sorted(FILMS.items()))
    with open(FILE_NAME, 'w', encoding='utf-8') as f:
        f.write(json.dumps(FILMS, ensure_ascii=False))
    print(f'Локальная фильмотека успешно сохранена в файл "{FILE_NAME}".')


def load():
    global FILMS
    with open(FILE_NAME, 'r', encoding='utf-8') as f:
        FILMS = json.load(f)
    print(f'Локальная фильмотека успешно загружена из файла "{FILE_NAME}".')


def erase():
    global FILMS
    FILMS.clear()
    print('Локальная фильмотека успешно очищена.')
    save()


def print_film(film):
    print()
    print(re.sub('(\],)|(\},)|[\{\}\[\]]|(?<=\],)\n|\n(\n)', '',
          json.dumps(film, ensure_ascii=False, indent=0)).strip())


def film_choice(films):
    film_index = -1
    print(*enumerate(films, start=1), sep='\n')
    for _ in range(3):
        try:
            film_index \
                = int(input(f'Фильм 1-{len(films)} (чтобы отменить выбор - 0): ')) - 1
            break
        except ValueError:
            print('Попробуйте ещё раз.')

    return film_index


def imdb_found(film_title):
    found_movies = []
    for _ in range(5):
        found_movies = IA.search_movie(film_title)
        if found_movies:
            break

    len_movies = min(5, len(found_movies))
    if found_movies:
        movies = found_movies[:len_movies]
    else:
        print(f'Фильм "{film_title}" не найден в IMDb.')
        return ''

    if len_movies > 1:
        print('Выберите фильм для добавления:')
        film_index = film_choice(movies)
    else:
        film_index = 0

    if film_index == -1:
        print('Фильм не выбран.')
        return ''

    return movies[film_index].movieID


def imdb_get(film_id):
    try:
        return IA.get_movie(film_id, info=['main', 'akas'])
    except IMDbError as e:
        print('Возникли ошибки при вызове сервиса IMDb:')
        print(*e.args, sep='\n')
        return


def add_film_imdb(f_title):
    film_id = imdb_found(f_title)
    if not film_id:
        print('Операция добавления фильма отменена.')
        return

    film_info = imdb_get(film_id)
    if not film_info:
        print('Операция добавления фильма отменена.')
        return

    film_title = film_info['long imdb title']

    if film_info['original title'] != film_info['title']:
        film_title += ' / ' + film_info['original title']

    rus_titles = [title for title in film_info['akas'] if 'Rus' in title]
    rus_title = rus_titles[0] if rus_titles else ''
    rus_title = rus_title.replace(' Russia', '')
    rus_title = rus_title.replace(' Soviet Union (Russian title)', '')
    if rus_title:
        film_title += ' / ' + rus_title

    film_keys = ['title', 'original title', 'year', 'rating', 'genres']
    FILMS[film_title] = {'rus_title': rus_title}
    FILMS[film_title].update({k: film_info[k] for k in film_keys})

    for k in ['director', 'writer']:
        FILMS[film_title][k] = [v['name'] if v.personID else ''
                                for v in film_info[k]] if k in film_info else ['']

    FILMS[film_title]['date_added'] = datetime.today().isoformat(timespec='seconds')
    print()
    print('Фильм успешно добавлен в локальную фильмотеку:')
    print_film({film_title: FILMS[film_title]})


def find_by_title(f_title):
    f_search = f_title.lower().replace(' ', '.*').strip()
    return {k: v for k, v in FILMS.items() if f_search in k.lower()}


def find_film(f_title):
    search_result = find_by_title(f_title)
    if search_result:
        print('Найдено несколько фильмов' if len(search_result) > 1
              else 'Фильм найден', 'в локальной фильмотеке:')
        print_film(search_result)
    else:
        print('Фильм не найден в локальной фильмотеке.')
        answer = input('Добавить фильм из IMDb? (y/n): ')
        search_imdb = answer == 'y' or answer == '1'
        if search_imdb:
            add_film_imdb(f_title)
        else:
            print('Операция добавления фильма отменена.')
            return


def remove_film_by_key(k):
    try:
        del FILMS[k]
        print(f'Фильм "{k}" успешно удалён из локальной фильмотеки.')
    except KeyError as e:
        print('Возникли ошибки при удалении фильма:')
        print(*e.args, sep='\n')


def remove_film(f_title):
    search_result = find_by_title(f_title)
    if len(search_result) > 1:
        print('Найдено несколько фильмов.')
        del_all = input('Удалить все? (y/n): ') == 'y'
        if del_all:
            for k in search_result:
                remove_film_by_key(k)
        else:
            print('Выберите фильм для удаления:')
            film_index = film_choice(search_result)
            if film_index == -1:
                print('Фильм не выбран. Операция удаления фильма отменена.')
                return
            remove_film_by_key(list(search_result.keys())[film_index])
    elif search_result:
        remove_film_by_key(list(search_result.keys())[0])
    else:
        print(f'Фильм "{f_title}" не найден в локальной фильмотеке.')
        return


def help():
    print('/all - вывести текущий список всех фильмов')
    print('/add - добавить фильм в коллекцию')
    print('/film - вывести информацию о фильме')
    print('/remove - удалить файл из коллекции')
    print('/save - сохранить фильмотеку в файл')
    print('/load - загрузить фильмотеку из файла')
    print('/erase - очистить всю локальную фильмотеку')
    print('/stop - остановить бота')
    print('/stop+ - сохранить фильмотеку и остановить бота')
    print('/help - вывести этот мануал')


def stop_bot():
    print('Бот остановил свою работу. Заходите ещё, будем рады!')
    exit()


def start_bot():
    print('Бот-фильмотека начал свою работу')
    print()
    while True:
        command = input('Введите команду: ')
        if command == '/stop':
            stop_bot()
        if command == '/stop+':
            save()
            stop_bot()
        elif command == '/all':
            if FILMS:
                print()
                print('Текущий список всех фильмов:')
                print_film(FILMS)
            else:
                print()
                print('В фильмотеке ещё нет фильмов.',
                      'Чтобы добавить фильм используйте команду /add.')
        elif command == '/add' or command == '/film':
            f = input('Введите название фильма: ')
            print()
            find_film(f)
        elif command == '/remove':
            f = input('Введите название фильма для удаления: ')
            print()
            remove_film(f)
        elif command == '/random':
            print('Случайный фильм:')
            print_film(random.choice(FILMS))
        elif command == '/save':
            save()
        elif command == '/load':
            print('Внимание! Все несохранённые изменения будут потеряны!')
            if input(f'Выполнить загрузку фильмотеки из файла "{FILE_NAME}"? (y/n): ') == 'y':
                load()
            else:
                print('Загрузка из файла отменена.')
        elif command == '/erase':
            print('Внимание! Это действие необратимо!',
                  'Вся локальная фильмотека будет очищена.')
            if input(f'Очистить всю локальную фильмотеку в файле "{FILE_NAME}"? (y/n): ') == 'y':
                erase()
            else:
                print('Полная очистка фильмотеки отменена.')
        elif command == '/help':
            help()
        else:
            print('Неопознанная команда. Просьба изучить мануал через /help')
        print()


def main():
    command = input('Введите /start для начала работы с ботом: ')
    if command == '/start':
        try:
            load()
        except Exception:
            print(f'Не удалось загрузить фильмотеку из файла "{FILE_NAME}".')
        start_bot()
    else:
        stop_bot()


if __name__ == '__main__':
    main()
