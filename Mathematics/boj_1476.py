e, s, m = map(int, input().split())
i = 1
while True:
    if (i-1) % 15 == e-1 and (i-1) % 28 == s-1 and (i-1) % 19 == m-1:
        print(i)
        break
    i += 1
