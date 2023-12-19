def merge(line):
    non_zero = [i for i in line if i != 0]
    merged = []
    i = 0
    while i < len(non_zero):
        if i + 1 < len(non_zero) and non_zero[i] == non_zero[i + 1]:
            merged.append(non_zero[i] * 2)
            i += 2
        else:
            merged.append(non_zero[i])
            i += 1
    return merged + [0] * (len(line) - len(merged))


def move(board, direction):
    new_board = [[0] * n for _ in range(n)]
    if direction == 'u':
        for j in range(n):
            col = [board[i][j] for i in range(n)]
            merged = merge(col)
            for i in range(n):
                new_board[i][j] = merged[i]
    elif direction == 'd':
        for j in range(n):
            col = [board[i][j] for i in range(n)]
            merged = merge(col[::-1])[::-1]
            for i in range(n):
                new_board[i][j] = merged[i]
    elif direction == 'l':
        for i in range(n):
            merged = merge(board[i])
            new_board[i] = merged
    elif direction == 'r':
        for i in range(n):
            merged = merge(board[i][::-1])[::-1]
            new_board[i] = merged
    return new_board


def solution(board, moves):
    if moves == 5:
        return max(max(row) for row in board)

    max_value = 0
    for direction in ['u', 'd', 'l', 'r']:
        new_board = move(board, direction)
        max_value = max(max_value, solution(new_board, moves + 1))

    return max_value


n = int(input())
example_board = [list(map(int, input().split())) for _ in range(n)]

max_value = solution(example_board, 0)
print(max_value)

