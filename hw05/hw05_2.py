# задача 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления
# данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

import re


def save_file(file_name, txt):
    try:
        with open(file_name, 'w', encoding='utf-8') as f:
            f.write(txt)
            print(f'File {file_name} saved successfully!')
    except Exception as ex:
        print(f'Error saving {file_name} file!')
        exit(ex)


def read_file(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as f:
            return f.read()
    except OSError as ex:
        print('File does not exist!')
        exit(ex)


def rle_encode(word):
    r = 0
    start = 0
    encoded_word = ''
    for i in range(len(word) - 1):
        if word[i] == word[i + 1]:
            if r < 0:
                encoded_word += str(r if r < -1 else 1) + word[start:i]
                r = 0
            r += 1
        else:
            if r > 0:
                encoded_word += str(r + 1) + word[i]
                r = 0
                start = i + 1
            else:
                r -= 1

    if r >= 0 and word:
        encoded_word += str(r + 1) + word[-1]
    elif r < 0:
        encoded_word += str(r - 1 if r < 0 else 1) + word[start:]

    return encoded_word


def rle_decode(encoded_word):
    rle_pattern = '(\-?\d+)([^\d-]+)'
    groups = re.findall(rle_pattern, encoded_word)
    return ''.join([s * int(r) if int(r) > 0 else s for r, s in groups])


def main():
    file_name = input('Input filename to encode with RLE algorithm: ').strip()
    original_text = read_file(file_name)
    encoded_text = rle_encode(original_text)
    decoded_text = rle_decode(encoded_text)
    save_file('encoded_file.txt', encoded_text)
    save_file('decoded_file.txt', decoded_text)
    print(f'original_text == decoded_text is {original_text == decoded_text}')


if __name__ == '__main__':
    main()
