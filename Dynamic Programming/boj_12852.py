n = int(input())

dp = [0] * (n + 1)
li = [0] * (n + 1)

for i in range(2, n + 1):
    dp[i] = dp[i - 1] + 1
    li[i] = i - 1
    if i % 2 == 0 and dp[i] > dp[i // 2] + 1:
        dp[i] = dp[i // 2] + 1
        li[i] = i // 2
    if i % 3 == 0 and dp[i] > dp[i // 3] + 1:
        dp[i] = dp[i // 3] + 1
        li[i] = i // 3

print(dp[n])

num = n
print(num, end=' ')
while num > 1:
    print(li[num], end=' ')
    num = li[num]

