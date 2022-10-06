from collections import deque
import sys

input = sys.stdin.readline

m, n = map(int, input().split())
graph = [list(map(int ,input().split())) for _ in range(n)]

d = deque()
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            d.append([i, j])

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs():
    while d:
        x, y = d.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                d.append([nx, ny])
                graph[nx][ny] = graph[x][y] + 1

bfs()
ans = 0
for g in graph:
    for i in g:
        if i == 0:
            print(-1)
            exit(0)
        ans = max(ans, i)
print(ans-1)
