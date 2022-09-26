import sys

input = sys.stdin.readline

n = int(input())

graph = [[0]*(n+1) for _ in range(n+1)]
visited = [0]*(n+1)

m = int(input())

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

def bfs(V):
    q = [V]
    visited[V] = 1
    while q:
        V = q.pop(0)
        for i in range(1, n+1):
            if graph[V][i] == 1 and visited[i] == 0:
                q.append(i)
                visited[i] = 1

bfs(1)
cnt = 0
for i in visited:
    if i:
        cnt += 1

print(cnt-1)
