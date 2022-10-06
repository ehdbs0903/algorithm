import sys

input = sys.stdin.readline

n, m, v = map(int, input().split())

graph = [[0]*(n+1) for _ in range(n+1)]
visited = [0]*(n+1)
visited2 = [0]*(n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

def dfs(V):
    visited[V] = 1
    print(V, end = ' ')
    for i in range(n+1):
        if graph[V][i] == 1 and visited[i] == 0:
            dfs(i)

def bfs(V):
    q = [V]
    visited2[V] = 1
    while q:
        V = q.pop(0)
        print(V, end = ' ')
        for i in range(n+1):
            if graph[V][i] == 1 and visited2[i] == 0:
                q.append(i)
                visited2[i] = 1

dfs(v)
print()
bfs(v)
