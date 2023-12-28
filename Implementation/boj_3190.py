import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

board = [[0] * n for _ in range(n)]
board[0][0] = 2

k = int(input())
for _ in range(k):
    i, j = map(int, input().split())
    board[i-1][j-1] = 1

rotation = deque()

l = int(input())
for _ in range(l):
    x, c = input().rstrip().split()
    rotation.append([int(x), c])


def rotate_direction(direction, c):
    if c == 'L':
        direction.rotate(1)
    else:
        direction.rotate(-1)


def move_snake(x, y, direction, time, current_rotation):
    x += direction[0][0]
    y += direction[0][1]
    time += 1
    if current_rotation < l and time >= rotation[current_rotation][0]:
        rotate_direction(direction, rotation[current_rotation][1])
        current_rotation += 1

    return x, y, time, current_rotation


def game():
    head_time = tail_time = 0
    head_x, head_y = 0, 0
    tail_x, tail_y = 0, 0
    head_rotation = tail_rotation = 0
    head_direction = deque([[0, 1], [1, 0], [0, -1], [-1, 0]])
    tail_direction = deque([[0, 1], [1, 0], [0, -1], [-1, 0]])

    while True:
        head_x, head_y, head_time, head_rotation =\
            move_snake(head_x, head_y, head_direction, head_time, head_rotation)

        if 0 > head_x or head_x >= n or 0 > head_y or head_y >= n:
            break

        if board[head_x][head_y] == 2:
            break

        if board[head_x][head_y] == 0:
            board[tail_x][tail_y] = 0
            tail_x, tail_y, tail_time, tail_rotation = \
                move_snake(tail_x, tail_y, tail_direction, tail_time, tail_rotation)

        board[head_x][head_y] = 2

    print(head_time)


game()

