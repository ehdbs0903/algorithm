import sys

input = sys.stdin.readline


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


n, m = map(int, input().split())
e_list = [list(map(int, input().split())) for _ in range(m)]
parent = [i for i in range(n+1)]

e_list.sort(key=lambda x: x[2])

cost = 0
for a, b, c in e_list:
    cost += c
    p1, p2 = find(a), find(b)

    if p1 != p2:
        if p1 > p2:
            parent[p1] = p2
        else:
            parent[p2] = p1
        cost -= c

for i in range(2, n+1):
    if parent[i] == i:
        cost = -1

print(cost)

