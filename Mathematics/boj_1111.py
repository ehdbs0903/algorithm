n = int(input())
nums = list(map(int, input().split()))

if n <= 1:
    print('A')

elif n == 2:
    print('A' if nums[1] != nums[0] else nums[0])

else:
    a = (nums[2] - nums[1]) // (nums[1] - nums[0]) if nums[1] - nums[0] else 0
    b = nums[2] - nums[1] * a

    for i in range(1, n):
        if nums[i-1] * a + b != nums[i]:
            print('B')
            exit()

    print(nums[-1] * a + b)

