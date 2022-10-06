import sys

input = sys.stdin.readline

n = int(input())

line = [0] * n
for i in range(n):
    line[i] = list(map(int, input().split()))
line.sort()
dp = [0] * n
for i in range(n):
    for j in range(i):
        if line[i][1] > line[j][1] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1

print(n - max(dp))
