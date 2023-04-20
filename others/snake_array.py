# Вывести двумерный массив змейкой
# На вход подается размер массива nxm
# Массив заполняется цифрами по возрастанию с шагом 1

def run():
    print()
    matrix = __zmeyka(5, 7)

    for row in matrix:
        for col in row:
            print(f'{col} ', end='')
        print()


def __zmeyka(n, m) -> []:
    matrix = []
    number = 0

    for i in range(0, n):
        items = []
        for j in range(0, m):
            items.append(number)
            number += 1
        if i % 2 > 0:
            __reverse(items)
        matrix.append(items)

    return matrix


def __reverse(items: []):
    n = len(items) - 1
    a = n // 2
    for i in range(0, a):
        items[n - i], items[i] = items[i], items[n - i]