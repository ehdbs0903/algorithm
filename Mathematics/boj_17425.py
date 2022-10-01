import sys

input = sys.stdin.readline

MAX = 1000000
dp = [1] * (MAX + 1)
prefix_sum = [0] * (MAX + 1)

for i in range(2, MAX + 1):
    j = 1
    while i * j <= MAX:
        dp[i * j] += i
        j += 1

for i in range(1, MAX + 1):
    prefix_sum[i] = prefix_sum[i - 1] + dp[i]

for _ in range(int(input())):
    n = int(input())
    print(prefix_sum[n])

