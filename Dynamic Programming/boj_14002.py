n = int(input())
nums = list(map(int, input().split()))

dp = [1] * n

for i in range(n):
    for j in range(i):
        if nums[i] > nums[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))

li = []
order = max(dp)
for i in reversed(range(n)):
    if dp[i] == order:
        li.append(nums[i])
        order -= 1

li.reverse()
print(*li)

