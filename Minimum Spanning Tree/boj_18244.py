import sys

input = sys.stdin.readline


def find(v):
    if parent[v] != v:
        parent[v] = find(parent[v])
    return parent[v]


n, m, k = map(int, input().split())
generator = list(map(int, input().split()))
edges = [list(map(int, input().split())) for _ in range(m)]
parent = [0 if i in generator else i for i in range(n+1)]

edges.sort(key=lambda x: x[2])

ans = 0
for a, b, w in edges:
    parent_a = find(a)
    parent_b = find(b)

    if parent_a != parent_b:
        ans += w
        if parent_a > parent_b:
            parent[parent_a] = parent_b
        else:
            parent[parent_b] = parent_a

print(ans)

