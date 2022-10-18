import sys

input = sys.stdin.readline


def find(v):
    if parent[v] != v:
        parent[v] = find(parent[v])
    return parent[v]


n = int(input())
points = [[*map(int, input().split()), i] for i in range(n)]
parent = [i for i in range(n)]
elist = []

for i in range(3):
    points.sort(key=lambda x: x[i])
    for j in range(1, n):
        elist.append([abs(points[j][i] - points[j - 1][i]), points[j][3], points[j - 1][3]])

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

print(ans)

