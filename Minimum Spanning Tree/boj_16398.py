import sys

input = sys.stdin.readline


def find(v):
    if parent[v] != v:
        parent[v] = find(parent[v])
    return parent[v]


n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
parent = [i for i in range(n + 1)]
elist = []

for i in range(n):
    for j in range(i + 1, n):
        elist.append([matrix[i][j], i, j])

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

