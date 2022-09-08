import sys

input = sys.stdin.readline

n, m = map(int, input().split())
board = [[0] * (m + 1)] + [[0] + list(map(int, input().split())) for _ in range(n)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        board[i][j] += max(board[i-1][j], board[i][j-1])

print(board[-1][-1])
