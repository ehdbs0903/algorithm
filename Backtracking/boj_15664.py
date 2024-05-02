n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))

arr = []

def backtracking(idx):
    if len(arr) == m:
        print(*arr)
        return
    overlap = 0
    for i in range(idx, n):
        if overlap != nums[i]:
            arr.append(nums[i])
            overlap = nums[i]
            backtracking(i + 1)
            arr.pop()

backtracking(0)
