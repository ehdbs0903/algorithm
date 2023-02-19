n = int(input())

nums = [0, 1, 1] + [0] * (n-2)

for i in range(3, n+1):
    nums[i] = nums[i-1] + nums[i-2]

print(nums[n])
