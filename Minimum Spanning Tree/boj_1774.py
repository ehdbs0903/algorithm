import sys
import math

input = sys.stdin.readline


def find(v):
    if parent[v] != v:
        parent[v] = find(parent[v])
    return parent[v]


n, m = map(int, input().split())
points = [list(map(int, input().split())) for _ in range(n)]
parent = [i for i in range(n + 1)]
elist = []

for i in range(n):
    for j in range(i + 1, n):
        x1, y1, x2, y2 = points[i][0], points[i][1], points[j][0], points[j][1]
        w = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        elist.append([w, i + 1, j + 1])

elist.sort()

for _ in range(m):
    a, b = map(int, input().split())
    parent_a = find(a)
    parent_b = find(b)

    if parent_a > parent_b:
        parent[parent_a] = parent_b
    else:
        parent[parent_b] = parent_a

ans = 0
for w, v1, v2 in elist:
    parent_v1 = find(v1)
    parent_v2 = find(v2)

    if parent_v1 != parent_v2:
        if parent_v1 > parent_v2:
            parent[parent_v1] = parent_v2
        else:
            parent[parent_v2] = parent_v1
        ans += w

print("{:.2f}".format(ans))

