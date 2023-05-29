import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [[0] * (m + 1)] + [[0] + list(map(int, input().split())) for _ in range(n)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        arr[i][j] = arr[i][j-1] + arr[i-1][j] - arr[i-1][j-1] + arr[i][j]

k = int(input())
for _ in range(k):
    i, j, x, y = map(int, input().split())
    print(arr[x][y] - arr[x][j - 1] - arr[i - 1][y] + arr[i - 1][j - 1])