n, m = map(int, input().split())
nums = sorted(list(set(map(int, input().split()))))

arr = []

def backtracking(idx):
    if len(arr) == m:
        print(*arr)
    else:
        for num in nums:
            if len(arr) == 0 or num >= arr[-1]:
                arr.append(num)
                backtracking(idx + 1)
                arr.pop()

backtracking(0)
