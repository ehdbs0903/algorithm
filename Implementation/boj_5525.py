n = int(input())
m = int(input())
s = input()

cnt = 0
i = 0

while i < (m - 1):
    if s[i:i + 3] == "IOI":
        k = 0
        while i + 2 < m and s[i:i + 3] == "IOI":
            k += 1
            i += 2
        if k >= n:
            cnt += k - n + 1
    else:
        i += 1

print(cnt)
