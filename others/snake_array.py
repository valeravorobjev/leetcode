# Вывести двумерный массив змейкой
# На вход подается размер массива nxm
# Массив заполняется цифрами по возрастанию с шагом 1

def run():
    print()
    n = 5
    m = 7
    matrix = __snake2(n, m)

    lj = len(f'{n * m}') + 1

    for row in matrix:
        for col in row:
            print(f'{col}'.ljust(lj), end='')
        print()


def __snake1(n, m) -> []:
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


def __snake2(n, m) -> []:
    # init
    matrix = []
    for i in range(0, n):
        items = []
        for j in range(0,m):
            items.append(0)
        matrix.append(items)

    # algorithm

    top = True
    left = False
    right = False
    bottom = False

    size = n*m
    number = 0

    row_start = 0
    row_end = n

    col_start = 0
    col_end = m

    while number < size:
        if top:
            for i in range(col_start, col_end):
                number +=1
                matrix[row_start][i] = number

            row_start +=1
            top = False
            right = True

        elif right:
            for i in range(row_start, row_end):
                number += 1
                matrix[i][col_end - 1] = number

            right = False
            bottom = True
            col_end += -1

        elif bottom:
            for i in range(col_end, col_start, -1):
                number += 1
                matrix[row_end - 1][i-1] = number

            bottom = False
            left = True
            row_end -= 1

        elif left:
            for i in range(row_end, row_start, -1):
                number += 1
                matrix[i-1][col_start] = number

            left = False
            top = True

            col_start += 1

    return matrix

def __reverse(items: []):
    n = len(items) - 1
    a = n // 2
    for i in range(0, a):
        items[n - i], items[i] = items[i], items[n - i]
