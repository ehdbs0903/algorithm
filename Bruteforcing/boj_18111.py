import sys

input = sys.stdin.readline

n, m, b = map(int, input().split())
blocks = [list(map(int, input().split())) for _ in range(n)]
time, height = float('inf'), 0
for h in range(257):
    t = 0
    bb = b
    for i in range(n):
        for j in range(m):
            diff = h - blocks[i][j]
            if diff >= 0:
                t += diff
                bb -= diff
            else:
                t -= diff * 2
                bb -= diff
    if bb >= 0:
        if time >= t:
            time = t
            height = h

print(time, height)
