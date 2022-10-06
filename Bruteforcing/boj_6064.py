import sys

input = sys.stdin.readline

for _ in range(int(input())):
    m, n, x, y = map(int, input().split())
    while x <= m * n:
        if x % n == y % n:
            print(x)
            break
        x += m
    else:
        print(-1)

