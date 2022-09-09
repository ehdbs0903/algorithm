import sys

input = sys.stdin.readline

n, m = map(int, input().split())

prefix = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
for i in range(1, n + 1):
    board = list(map(int, input().split()))
    temp = 0
    for j in range(1, n + 1):
        temp += board[j - 1]
        prefix[i][j] = temp + prefix[i-1][j]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    print(prefix[x2][y2] - prefix[x2][y1 - 1] - prefix[x1 - 1][y2] + prefix[x1 - 1][y1 - 1])
