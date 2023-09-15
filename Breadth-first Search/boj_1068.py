from collections import deque

n = int(input())
parent = list(map(int, input().split()))

graph = [[] for _ in range(n)]
for i in range(n):
    if parent[i] == -1:
        continue
    graph[parent[i]].append(i)


def bfs(v):
    parent[v] = -2
    q = deque([v])

    while q:
        v = q.popleft()

        for nv in graph[v]:
            parent[nv] = -2
            q.append(nv)


k = int(input())
bfs(k)
cnt = 0
for i in range(n):
    if parent[i] != -2 and i not in parent:
        cnt += 1

print(cnt)
