a = input()
b = input()

dp = [0] * len(b)

for i in range(len(a)):
    temp = 0
    for j in range(len(b)):
        if temp < dp[j]:
            temp = dp[j]
        elif a[i] == b[j]:
            dp[j] = temp + 1

print(max(dp))
