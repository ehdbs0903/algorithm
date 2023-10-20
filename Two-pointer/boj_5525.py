n = int(input())
m = int(input())
s = input()

cnt = 0
pattern_cnt = 0
i = 1

while i < m - 1:
    if s[i-1:i+2] == "IOI":
        pattern_cnt += 1
        if pattern_cnt == n:
            pattern_cnt -= 1
            cnt += 1
        i += 2
    else:
        pattern_cnt = 0
        i += 1

print(cnt)

