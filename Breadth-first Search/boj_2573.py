import sys
from collections import deque

input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def bfs(x, y):
    q = deque()
    q.append([x, y])
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] > 0 and not visited[nx][ny]:
                    q.append([nx, ny])
                    visited[nx][ny] = 1
                elif graph[nx][ny] <= 0:
                    w[x][y] += 1


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

time = 0
while True:
    visited = [[0] * m for _ in range(n)]
    w = [[0] * m for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] > 0 and not visited[i][j]:
                bfs(i, j)
                cnt += 1

    for i in range(n):
        for j in range(m):
            graph[i][j] -= w[i][j]

    time += 1
    if cnt >= 2:
        print(time - 1)
        break
    elif not cnt:
        print(0)
        break

