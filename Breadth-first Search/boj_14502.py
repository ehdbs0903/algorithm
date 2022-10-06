import math

n = int(input())
nums = list(map(int, input().split()))

cnt = 0
for i in nums:
    if i == 1:
        cnt += 1
    else:
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                cnt += 1
                break
print(len(nums) - cnt)[main 0f3aafb] Add mathematics/boj_1978.py
import math

n = int(input())
nums = list(map(int, input().split()))

cnt = 0
for i in nums:
    if i == 1:
        cnt += 1
    else:
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                cnt += 1
                break
print(len(nums) - cnt)
