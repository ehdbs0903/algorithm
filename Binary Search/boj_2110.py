import sys

input = sys.stdin.readline

n, c = map(int, input().split())
points = [int(input()) for _ in range(n)]

points.sort()
start, end = 1, points[-1] - points[0]
while start <= end:
    mid = (start + end) // 2

    cnt = 1
    temp = points[0]
    for p in points:
        if p - temp >= mid:
            cnt += 1
            temp = p

    if cnt < c:
        end = mid - 1
    else:
        start = mid + 1

print(end)
