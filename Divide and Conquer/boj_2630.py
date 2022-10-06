import sys

input = sys.stdin.readline


def recursion(x, y, m):
    global white, blue
    for i in range(x, x + m):
        for j in range(y, y + m):
            if board[i][j] != board[x][y]:
                recursion(x, y, m // 2)
                recursion(x, y + m // 2, m // 2)
                recursion(x + m // 2, y, m // 2)
                recursion(x + m // 2, y + m // 2, m // 2)
                return
    if board[x][y]:
        blue += 1
    else:
        white += 1


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

white = blue = 0
recursion(0, 0, n)

print(white)
print(blue)

