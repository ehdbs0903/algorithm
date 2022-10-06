import sys

input = sys.stdin.readline

sums = []
nums = []

n, m = map(int, input().split())

nums = list(map(int, input().split()))
sums.append(nums[0])

for i in range(1, n):
    sums.append(sums[i-1] + nums[i])

for _ in range(m):
    i, j = map(int, input().split())
    if i == 1:
        print(sums[j-1])
    else:
        print(sums[j-1] - sums[i-2])
