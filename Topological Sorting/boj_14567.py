import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
inDegree = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    inDegree[b] += 1

q = deque()
for i in range(1, n + 1):
    if not inDegree[i]:
        q.append(i)

ans = [0] * (n + 1)
while q:
    v = q.popleft()
    ans[v] += 1

    for g in graph[v]:
        inDegree[g] -= 1
        ans[g] = max(ans[v], ans[g])

        if not inDegree[g]:
            q.append(g)

print(*ans[1:])
