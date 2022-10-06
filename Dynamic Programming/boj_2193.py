n = int(input())

dp = [0, 1, 1, 2, 3]

for i in range(len(dp), n + 1):
    dp.append(dp[i - 1] + dp[i - 2])
print(dp[n])
