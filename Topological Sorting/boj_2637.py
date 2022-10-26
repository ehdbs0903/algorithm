import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
graph = [[] for _ in range(n + 1)]
cost = [[0] * (n + 1) for _ in range(n + 1)]
inDegree = [0] * (n + 1)

for _ in range(int(input())):
    x, y, k = map(int, input().split())
    graph[y].append((x, k))
    inDegree[x] += 1

q = deque()
for i in range(1, n + 1):
    if not inDegree[i]:
        q.append(i)

while q:
    v = q.popleft()

    for g, cnt in graph[v]:
        if cost[v].count(0) == n + 1:
            cost[g][v] += cnt
        else:
            for i in range(1, n + 1):
                cost[g][i] += cost[v][i] * cnt

        inDegree[g] -= 1
        if not inDegree[g]:
            q.append(g)

for ans in enumerate(cost[n]):
    if ans[1] > 0:
        print(*ans)

