import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
inDegree = [0] * (n + 1)

for _ in range(m):
    u, v = map(int, input().split())
    graph[v].append(u)
    inDegree[u] += 1

q = deque()
for i in range(1, n + 1):
    if not inDegree[i]:
        q.append(i)

ans = 0
while q:
    v = q.popleft()
    ans += 1

    for g in graph[v]:
        inDegree[g] -= 1

        if not inDegree[g]:
            q.append(g)

print(ans)

