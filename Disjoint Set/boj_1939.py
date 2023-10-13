import sys

input = sys.stdin.readline


def find(v):
    if parent[v] != v:
        parent[v] = find(parent[v])
    return parent[v]


def union(x, y):
    parent_x = find(x)
    parent_y = find(y)

    if parent_x != parent_y:
        parent[parent_y] = parent_x


n, m = map(int, input().split())
bridges = [list(map(int, input().split())) for _ in range(m)]

bridges.sort(key=lambda x: x[2], reverse=True)

parent = [i for i in range(n+1)]

p, q = map(int, input().split())

for a, b, c in bridges:
    union(a, b)
    if find(p) == find(q):
        print(c)
        break

