import sys

sys.setrecursionlimit(10**7)
input = sys.stdin.readline


def recursion(x, y, m):
    global zero, positive, negative

    for i in range(x, x + m):
        for j in range(y, y + m):
            if board[i][j] != board[x][y]:
                recursion(x, y, m // 3)
                recursion(x, y + m // 3, m // 3)
                recursion(x, y + m * 2 // 3, m // 3)
                recursion(x + m // 3, y, m // 3)
                recursion(x + m // 3, y + m // 3, m // 3)
                recursion(x + m // 3, y + m * 2 // 3, m // 3)
                recursion(x + m * 2 // 3, y, m // 3)
                recursion(x + m * 2 // 3, y + m // 3, m // 3)
                recursion(x + m * 2 // 3, y + m * 2 // 3, m // 3)
                return

    if board[x][y] == 1:
        positive += 1
    elif board[x][y] == -1:
        negative += 1
    else:
        zero += 1


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

zero = positive = negative = 0
recursion(0, 0, n)

print(negative)
print(zero)
print(positive)

