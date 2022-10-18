import sys

input = sys.stdin.readline


def find(v):
    if parent[v] != v:
        parent[v] = find(parent[v])
    return parent[v]


n = int(input())
m = int(input())
elist = [list(map(int, input().split())) for _ in range(m)]
parent = [i for i in range(n + 1)]

elist.sort(key=lambda x: x[2])

ans = 0
for v1, v2, w in elist:
    parent_v1 = find(v1)
    parent_v2 = find(v2)

    if parent_v1 != parent_v2:
        if parent_v1 > parent_v2:
            parent[parent_v1] = parent_v2
        else:
            parent[parent_v2] = parent_v1
        ans += w

print(ans)

