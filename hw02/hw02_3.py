# 3. Напишите программу, в которой пользователь будет задавать две строки,
# а программа - определять количество вхождений одной строки в другой.

def count_occurences(str1, str2):
    len1 = len(str1)
    len2 = len(str2)
    count = 0
    i = 0
    if len1 >= len2:
        while i < len1 - len2 + 1:
            if str1[i:len2+i] == str2:
                count += 1
                i += len2
            i += 1
        return count, 0
    else:
        while i < len2 - len1 + 1:
            if str2[i:len1+i] == str1:
                count += 1
                i += len1
            i += 1
        return count, 1


def main():
    s1 = input('Input string 1: ')
    s2 = input('Input string 2: ')

    num, idx = count_occurences(s1, s2)
    print(f'The number of occurences of string {1 if idx else 2} in',
          f'string {2 if idx else 1} is {num}')


if __name__ == '__main__':
    main()
