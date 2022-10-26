# задача 5 необязательная Дан список чисел. Создайте список, в который попадают
# числа, описывающие максимальную возрастающую последовательность. Порядок
# элементов менять нельзя.

# *Пример:*
# [1, 5, 2, 3, 4, 6, 1, 7] => [1,  7]
# [1, 5, 2, 3, 4,  1, 7, 8 , 15 , 1 ] => [1,  5]

def find_largest_asc_sequence(seq):

    if not seq:
        return seq, 'Empty list', 0, 0

    try:
        iter(seq)
    except TypeError:
        return seq, 'Not iterable', 0, 0

    if not (isinstance(seq, list) or isinstance(seq, range)):
        try:
            temp_list = list(map(int, seq))
        except ValueError:
            return seq, 'Only numbers are accepted in the list', 0, 0
    else:
        temp_list = seq

    try:
        max_el = max(temp_list)
    except TypeError:
        return seq, 'Only numbers are accepted in the list', 0, 0

    res = [0] * 2
    temp_res = 0
    max_seq_len = 0
    left = set(temp_list)
    count = 0

    while left:
        max_seq = False
        min_el = min(left)
        to_remove = {min_el}

        for i in range(1, int(max_el) - int(min_el) + 1):
            count += 1
            if min_el + i in temp_list:
                temp_res = min_el + i
                if i + 1 > max_seq_len:
                    max_seq_len = i + 1
                    max_seq = True
                    to_remove.add(temp_res)
            else:
                break

        if max_seq:
            res[0] = min_el
            res[1] = temp_res

        left.difference_update(to_remove)

    return temp_list, res if res[1] else 'No sequence', len(temp_list), count


def main():
    tests = []
    tests.append([1, 5, 2, 3, 4, 6, 1, 7])
    tests.append([1, 2, 8, 12, 3, 4, 1, 7])
    tests.append([1, 5, 3, 4, 6, 1, 7])
    tests.append([1, 5.5, 3.4, 4.5, 6.5, 2.4, 7])
    tests.append([1, 5, 3, 6, 1])
    tests.append([1, 5, [3], 6, 1])
    tests.append(list(range(1, 11)))
    tests.append(range(1, 11))
    tests.append(map(lambda x: x + 1, range(1, 11)))
    tests.append(range(100))
    tests.append('21415875983')
    tests.append('21415875983fff')
    tests.append({21415875983})
    tests.append(21415875983)
    tests.append(())

    for test_list in tests:
        result = find_largest_asc_sequence(test_list)
        print(f'Input value: {test_list}, type: {type(test_list)}')
        print('Largest ascending sequence in list:',
              f'{result[0]} => {result[1]}',
              f'List length: {result[2]}',
              f'Number of iterations: {result[3]}',
              sep='\n')
        print()


if __name__ == '__main__':
    main()
