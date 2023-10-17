import sys

input = sys.stdin.readline


def find(v):
    if parent[v] != v:
        parent[v] = find(parent[v])
    return parent[v]


def union(x, y):
    parent_x = find(x)
    parent_y = find(y)

    if parent_x <= parent_y:
        parent[parent_y] = parent_x
    else:
        parent[parent_x] = parent_y


n = int(input())
m = int(input())

friend = []
enemy = []
enemy_list = [[] for _ in range(n+1)]

for _ in range(m):
    s, p, q = input().split()
    p, q = int(p), int(q)
    if s == 'F':
        friend.append([p, q])
    else:
        enemy.append([p, q])
        enemy_list[p].append(q)
        enemy_list[q].append(p)

parent = [i for i in range(n+1)]

for a, b in friend:
    union(a, b)

for a, b in enemy:
    for e in enemy_list[a]:
        union(e, b)

    for e in enemy_list[b]:
        union(e, a)

groups = set()
for i in range(1, n + 1):
    groups.add(find(i))

print(len(groups))

