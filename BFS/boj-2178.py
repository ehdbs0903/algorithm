import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[0] * m for _ in range(n)]
for i in range(n):
    s = input().rstrip()
    for j in range(m):
        if s[j] == '1':
            graph[i][j] = 1

dx = [1, 0, -1 ,0]
dy = [0, 1, 0, -1]

def bfs(x, y):
    graph[x][y] = 1
    d = deque()
    d.append((x, y))
    while d:
        x, y = d.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                d.append((nx, ny))
    return graph[n-1][m-1]

print(bfs(0, 0))
