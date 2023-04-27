import sys
from collections import deque

input = sys.stdin.readline

n, m, r = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
d = deque()

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for g in graph:
    g.sort(reverse=True)

cnt = 1
def bfs(v):
    global cnt
    visited[v] = cnt
    cnt += 1
    d.append(v)
    while d:
        u = d.popleft()
        for i in graph[u]:
            if visited[i] == 0:
                visited[i] = cnt
                cnt += 1
                d.append(i)

bfs(r)
for i in range(1, n+1):
    print(visited[i])
