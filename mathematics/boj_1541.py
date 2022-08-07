s = list(input().split("-"))
ans = 0
for i in range(len(s)):
    for j in s[i].split("+"):
        if i == 0:
            ans += int(j)
        else:
            ans -= int(j)
print(ans)
