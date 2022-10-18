import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def union(x, y):
    if x > y:
        parent[x] = y
    else:
        parent[y] = x


def find(v):
    if parent[v] != v:
        parent[v] = find(parent[v])
    return parent[v]


n, m = map(int, input().split())
parent = [i for i in range(n + 1)]

for _ in range(m):
    op, a, b = map(int, input().split())

    parent_a = find(a)
    parent_b = find(b)

    if op:
        if parent_a == parent_b:
            print("YES")
        else:
            print("NO")

    else:
        union(parent_a, parent_b)

