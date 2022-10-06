import sys

input = sys.stdin.readline

n, k = map(int, input().split())

nums = list(map(int, input().split()))
temp = 0
for i in range(k):
    temp += nums[i]
sums = [temp]

for i in range(k, n):
    sums.append(sums[i - k] - nums[i - k] + nums[i])

print(max(sums))
