import sys

input = sys.stdin.readline


def union(a, b):
    parent_a = find(a)
    parent_b = find(b)

    if parent_a > parent_b:
        parent[parent_a] = parent_b
    else:
        parent[parent_b] = parent_a


def find(v):
    if parent[v] != v:
        parent[v] = find(parent[v])
    return parent[v]


n = int(input())
m = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
travel = list(map(int, input().split()))
parent = [i for i in range(n)]

for i in range(n):
    for j in range(i + 1, n):
        if matrix[i][j]:
            union(i, j)

p = find(travel[0] - 1)
for i in range(1, m):
    temp = find(travel[i] - 1)

    if p != temp:
        print("NO")
        break

else:
    print("YES")

