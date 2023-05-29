import sys
from math import sqrt

input = sys.stdin.readline

n = int(input())

points = [list(map(int, input().split())) for _ in range(n)]

cnt = 0

for i in range(n - 1):
    for j in range(i + 1, n):
        cnt += sqrt((points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2)

print(2 * cnt / n)
