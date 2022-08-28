N = int(input())

dp = [0, 1, 2]

def fib(n):
    global dp
    dp += [0] * (n-2)
    if n == 1:
        return 1
    if n == 2:
        return 2
    for i in range(3, n+1):
        dp[i] = (dp[i-1] + dp[i-2]) % 15746
    return dp[n]

print(fib(N))
