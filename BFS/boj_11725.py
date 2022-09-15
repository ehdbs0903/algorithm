import sys
from collections import deque

input = sys.stdin.readline


def bfs(a):
    q = deque()
    q.append(a)
    visited[a] = 1
    while q:
        a = q.popleft()
        for g in graph[a]:
            if not visited[g]:
                q.append(g)
                visited[g] = a


n = int(input())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)

for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

bfs(1)

for i in range(2, n + 1):
    print(visited[i], end=' ')

