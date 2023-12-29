import sys
from collections import deque

input = sys.stdin.readline

EAST, WEST, NORTH, SOUTH = 1, 2, 3, 4
direction = [(0, 1), (0, -1), (-1, 0), (1, 0)]

n, m, x, y, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
moves = list(map(int, input().split()))

dice = deque([0] * 6)


def rotate_dice(d):
    if d == EAST:
        dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
    elif d == WEST:
        dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
    elif d == NORTH:
        dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]
    else:
        dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]


def simulation(x, y):
    for move in moves:
        nx = x + direction[move-1][0]
        ny = y + direction[move-1][1]

        if 0 > nx or nx >= n or 0 > ny or ny >= m:
            continue

        rotate_dice(move)

        if board[nx][ny] == 0:
            board[nx][ny] = dice[0]
        else:
            dice[0] = board[nx][ny]
            board[nx][ny] = 0

        x, y = nx, ny
        print(dice[5])


simulation(x, y)

