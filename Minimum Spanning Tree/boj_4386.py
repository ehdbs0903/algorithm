import sys
import math

input = sys.stdin.readline


def find(v):
    if parent[v] != v:
        parent[v] = find(parent[v])
    return parent[v]


n = int(input())
points = [list(map(float, input().split())) for _ in range(n)]
elist = []
parent = [i for i in range(n)]

for i in range(n):
    for j in range(i + 1, n):
        x1, y1, x2, y2 = points[i][0], points[i][1], points[j][0], points[j][1]
        w = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        elist.append([w, i, j])

elist.sort()

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

print(round(ans, 2))

