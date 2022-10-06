import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[0]*(n+1) for _ in range(n+1)]
visited = [0]*(n+1)

for _ in range(m):
    u, v = map(int, input().split())
    graph[u][v] = graph[v][u] = 1

def dfs(V):
    visited[V] = 1
    for i in range(1, n+1):
        if graph[V][i] == 1 and visited[i] == 0:
            dfs(i)

cnt = 0

for i in range(1, n+1):
    if visited[i] == 0:
        dfs(i)
        cnt += 1

print(cnt)
