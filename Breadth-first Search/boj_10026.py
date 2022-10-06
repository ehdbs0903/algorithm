import sys
from collections import deque

input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def bfs(x, y):
    q = deque()
    q.append([x, y])
    color = graph[x][y]
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == 0 and graph[nx][ny] == color:
                    visited[nx][ny] = 1
                    q.append([nx, ny])


n = int(input())

graph = [list(input().rstrip()) for _ in range(n)]

visited = [[0] * n for _ in range(n)]

cnt1 = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            bfs(i, j)
            cnt1 += 1

        if graph[i][j] == 'G':
            graph[i][j] = 'R'

visited = [[0] * n for _ in range(n)]
cnt2 = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            bfs(i, j)
            cnt2 += 1

print(cnt1, cnt2)

