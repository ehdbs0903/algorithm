from itertools import combinations

while True:
    nums = list(map(int, input().split()))
    if not nums[0]:
        break
    for i in combinations(nums[1:], 6):
        print(*i)
    print()
