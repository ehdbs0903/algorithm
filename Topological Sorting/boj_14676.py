import sys
from collections import deque

input = sys.stdin.readline

n, m, k = map(int, input().split())

graph = [[] for _ in range(n + 1)]
inDegree = [0] * (n + 1)
build = [0] * (n + 1)

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    inDegree[y] += 1

flag = 0
for _ in range(k):
    op, a = map(int, input().split())

    if op == 1:
        if inDegree[a]:
            flag = 1
            break

        build[a] += 1
        if build[a] == 1:
            for g in graph[a]:
                inDegree[g] -= 1

    else:
        if build[a] <= 0:
            flag = 1
            break

        build[a] -= 1
        if not build[a]:
            for g in graph[a]:
                inDegree[g] += 1

if flag:
    print("Lier!")
else:
    print("King-God-Emperor")

