n = int(input())

nums = [0, 1, 1]

def fibo(m):
    global nums
    nums += [0] * (m - 2)
    for i in range(3, m+1):
        nums[i] = nums[i-1] + nums[i-2]
    return nums[m]

print(fibo(n))
