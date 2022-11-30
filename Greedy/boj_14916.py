n = int(input())

cnt = n // 5
n = n % 5

while cnt > 0 and n % 2 != 0:
    cnt -= 1
    n += 5

cnt += n // 2
n = n % 2

if n != 0:
    print(-1)
else:
    print(cnt)

