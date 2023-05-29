import sys

input=sys.stdin.readline


def counting_paint(color):
    prefix = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n):
        for j in range(m):
            if (i+j) % 2 == 0:
                value = board[i][j] != color
            else:
                value = board[i][j] == color
            prefix[i+1][j+1] = prefix[i][j+1] + prefix[i+1][j] - prefix[i][j] + value

    count = int(1e9)
    for i in range(1, n-k+2):
        for j in range(1, m-k+2):
            count = min(count, prefix[i+k-1][j+k-1] - prefix[i+k-1][j-1] - prefix[i-1][j+k-1] + prefix[i-1][j-1])

    return count


n, m, k = map(int, input().split())

board = []
for i in range(n):
    board.append(list(input().rstrip()))

print(min(counting_paint('W'), counting_paint('B')))
