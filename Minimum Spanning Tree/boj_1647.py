import sys

input = sys.stdin.readline


def find(v):
    if parent[v] != v:
        parent[v] = find(parent[v])
    return parent[v]


n, m = map(int, input().split())
elist = [list(map(int, input().split())) for _ in range(m)]
parent = [i for i in range(n + 1)]

elist.sort(key=lambda x: x[2])

ans = 0
max_w = 0
for v1, v2, w in elist:
    a = find(v1)
    b = find(v2)

    if a != b:
        if a > b:
            parent[a] = b
        else:
            parent[b] = a
        ans += w
        max_w = w

print(ans - max_w)

