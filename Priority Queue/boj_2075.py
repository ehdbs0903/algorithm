import sys
import heapq

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

heapq.heapify(nums)

for _ in range(n-1):
    temp = list(map(int, input().split()))
    for t in temp:
        if t > nums[0]:
            heapq.heappop(nums)
            heapq.heappush(nums, t)

print(nums[0])

