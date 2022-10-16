binary_search(target):
    start, end = 0, len(lis) - 1

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
dp = [1] * n

for i in range(1, len(nums)):
    if lis[-1] < nums[i]:
        lis.append(nums[i])
        dp[i] = len(lis)
    else:
        j = binary_search(nums[i])
        lis[j] = nums[i]
        dp[i] = j + 1


idx = len(lis)
print(idx)

lis = [0] * idx
temp_idx = n - 1
while idx > 0:
    for i in range(temp_idx, -1, -1):
        if dp[i] == idx:
            lis[idx - 1] = nums[i]
            temp_idx = i
            break

    idx -= 1

print(*lis)

