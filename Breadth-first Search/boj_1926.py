import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    q = deque()
    q.append([x, y])
    visited[x][y] = 1
    area_cnt = 0
    while q:
        x, y = q.popleft()
        area_cnt += 1
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] and not visited[nx][ny]:
                q.append([nx, ny])
                visited[nx][ny] = 1

    return area_cnt


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

cnt = 0
area = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] and not visited[i][j]:
            area = max(area, bfs(i, j))
            cnt += 1

print(cnt)
print(area)


