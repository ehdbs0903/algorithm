import sys
import copy

input = sys.stdin.readline

dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]


def press_switch(x, y, map):
    for d in range(5):
        nx, ny = x + dx[d], y + dy[d]

        if 0 <= nx < 10 and 0 <= ny < 10:
            map[nx][ny] = '#' if map[nx][ny] == 'O' else 'O'


def generate_board():
    for a in range(2**10):
        new_board = copy.deepcopy(board)
        c = 0
        
        for b in range(10):
            if (a >> b) & 1:
                press_switch(0, b, new_board)
                c += 1

        yield c, new_board


board = [list(input().rstrip()) for _ in range(10)]

cnt_list = []
for c, ran_board in generate_board():
    cnt = c

    for i in range(1, 10):
        for j in range(10):
            if ran_board[i-1][j] == 'O':
                press_switch(i, j, ran_board)
                cnt += 1

    flag = 0
    for i in range(10):
        if ran_board[9][i] == 'O':
            flag = 1

    if flag:
        continue

    cnt_list.append(cnt)

print(min(cnt_list) if cnt_list else -1)

