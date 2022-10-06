import sys

input = sys.stdin.readline

n = int(input())

max_dp = [0] * 3
min_dp = [0] * 3

for i in range(n):
    tmp = list(map(int, input().split()))
    max_dp = [tmp[0] + max(max_dp[:2]), tmp[1] + max(max_dp), tmp[2] + max(max_dp[1:])]
    min_dp = [tmp[0] + min(min_dp[:2]), tmp[1] + min(min_dp), tmp[2] + min(min_dp[1:])]

print(max(max_dp), min(min_dp))

