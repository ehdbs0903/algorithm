from collections import deque

a, b = map(int, input().split())

q = deque()
q.append(b)
cnt = 1
while q:
    x = q.popleft()
    if x > a:
        if str(x)[-1] == '1':
            nx = int(str(x)[:-1])
            q.append(nx)
            cnt += 1

        if x % 2 == 0:
            nx = x // 2
            q.append(nx)
            cnt += 1

if x == a:
    print(cnt)
else:
    print(-1)

