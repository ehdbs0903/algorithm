def binary_search(target):
    start = 0
    end = len(lis) - 1

    while start <= end:
        mid = (start + end) // 2

        if lis[mid] == target:
            return mid
        elif lis[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return start


n = int(input())
nums = list(map(int, input().split()))

lis = [nums[0]]

for i in range(1, len(nums)):
    if lis[-1] < nums[i]:
        lis.append(nums[i])
    else:
        lis[binary_search(nums[i])] = nums[i]

print(len(lis))

