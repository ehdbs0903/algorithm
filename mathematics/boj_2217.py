import sys

input = sys.stdin.readline

n = int(input())

nums = [int(input()) for _ in range(n)]
nums.sort()

answer = []
for i in range(n):
    answer.append((n-i)*nums[i])
print(max(answer))
