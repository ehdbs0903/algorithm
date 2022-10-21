import sys

input = sys.stdin.readline

n, c = map(int, input().split())
x = [int(input()) for _ in range(n)]

x.sort()

start, end = 0, x[-1]
ans = 0

while start < end:
    mid = (start + end) // 2
    temp = x[0]
    cnt = 1

    for i in range(1, n):
        if x[i] - temp >= mid:
            cnt += 1
            temp = x[i]

    if cnt >= c:
        ans = mid
        start = mid + 1
    else:
        end = mid

print(ans)

