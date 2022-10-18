a = input()
b = input()

dp = [""] * len(b)

for i in range(len(a)):
    temp = ""

    for j in range(len(b)):
        if len(temp) < len(dp[j]):
            temp = dp[j]

        elif a[i] == b[j]:
            dp[j] = temp + b[j]

l, s = 0, ""
for d in dp:
    if len(d) > l:
        l = len(d)
        s = d

print(l)
print(s)

