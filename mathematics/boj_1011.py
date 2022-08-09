import sys
import math
input = sys.stdin.readline

t = int(input())
nums = [0]

n = 1
for _ in range(t):
    x, y = map(int, input().split())
    d = y - x
    if nums[-1] >= d:
        for i in range(len(nums)):
            if nums[i] >= d:
                print(i)
                break
    else:
        while True:
            nums.append(nums[n-1] + math.ceil(n/2))
            n += 1
            if nums[-1] >= d:
                print(len(nums)-1)
                break
