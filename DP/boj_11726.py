dp = [0, 1, 2, 3]

n = int(input())

for i in range(len(dp), n + 1):
    dp.append(dp[i - 1] + dp[i - 2])
print(dp[n] % 10007)
