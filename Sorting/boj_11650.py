n = int(input())

points = [list(map(int, input().split())) for _ in range(n)]

points.sort()

for p in points:
    print(*p)
