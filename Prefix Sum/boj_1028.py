import sys

input = sys.stdin.readline

r, c = map(int, input().split())
board = [input().rstrip() for _ in range(r)]

ld = [[0] * c for _ in range(r)]
rd = [[0] * c for _ in range(r)]

for i in range(r):
    for j in range(c):
        if board[i][j] == '1':
            if 0 <= i-1 and 0 <= j-1:
                rd[i][j] = rd[i-1][j-1] + 1
            else:
                rd[i][j] = 1
            if 0 <= i-1 and j+1 < c:
                ld[i][j] = ld[i-1][j+1] + 1
            else:
                ld[i][j] = 1

max_size = 0
for i in range(r):
    for j in range(c):

        for k in range(max_size, min(i, r - i, j, c - j) + 1):
            if not (0 <= i-k and i+k < r and 0 <= j-k and j+k < c):
                break

            if min(ld[i][j-k], ld[i+k][j], rd[i][j+k], rd[i+k][j]) >= k + 1:
                max_size = k + 1

print(max_size)

