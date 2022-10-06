n = int(input())
arr = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))

arr.sort()

def binary_search(num):
    l = 0
    r = n-1
    while l <= r :
        mid = (l+r)//2
        if arr[mid] == num :
            return 1
        elif arr[mid] > num :
            r = mid - 1
        else:
            l = mid + 1
    return 0

for num in arr2:
    print(binary_search(num), end = ' ')
