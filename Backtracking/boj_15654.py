n, m = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()
arr = []

def backtracking(idx):
    if len(arr) == m:
        print(*arr)
    else:
        for num in nums:
            if num not in arr:
                arr.append(num)
                backtracking(idx + 1)
                arr.pop()

backtracking(1)
