# задача 3. Напишите программу, удаляющую из текста все слова, содержащие "абв".
# Функции FIND и COUNT юзать нельзя.

def remove_words_with_text(str, seq):
    txt_list = str.split()
    for i in range(len(txt_list) - 1, -1, -1):
        if seq in txt_list[i]:
            del txt_list[i]

    return ' '.join(txt_list)


def main():
    txt = input('Input text: ')
    print(remove_words_with_text(txt, 'абв'))


if __name__ == '__main__':
    main()
