a = input()
b = input()
c = input()

m = len(a)
n = len(b)
p = len(c)

dp = [[[0] * (p + 1) for _ in range(n + 1)] for _ in range(m + 1)]

for i in range(1, m + 1):
    for j in range(1, n + 1):
        for k in range(1, p + 1):
            if a[i - 1] == b[j - 1] == c[k - 1]:
                dp[i][j][k] = dp[i - 1][j - 1][k - 1] + 1
            else:
                dp[i][j][k] = max(dp[i - 1][j][k], dp[i][j - 1][k], dp[i][j][k - 1])

print(dp[m][n][p])
