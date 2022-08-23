n = int(input())
nums = list(map(int, input().split()))
m = int(input())
targets = list(map(int, input().split()))

def binary_search(t, arr, left, right):
    if left > right:
        return 0
    mid = (left + right)//2
    if t == arr[mid]:
        return 1
    elif t < arr[mid]:
        return binary_search(t, arr, left, mid-1)
    else:
        return binary_search(t, arr, mid+1, right)

nums.sort()

for i in targets:
    left = 0
    right = len(nums)-1
    print(binary_search(i, nums, left, right))
