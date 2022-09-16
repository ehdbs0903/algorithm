import sys
from collections import deque

input = sys.stdin.readline

dx = [1, 0, -1, 0, 0, 0]
dy = [0, 1, 0, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

m, n, h = map(int, input().split())
graph = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
q = deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 1:
                q.append([i, j, k])

while q:
    x, y, z = q.popleft()
    for d in range(6):
        nx, ny, nz = x + dx[d], y + dy[d], z + dz[d]
        if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m and not graph[nx][ny][nz]:
            graph[nx][ny][nz] = graph[x][y][z] + 1
            q.append([nx, ny, nz])


flag = 1
max_num = 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 0:
                print(-1)
                exit(0)
            max_num = max(max_num, graph[i][j][k])

print(max_num - 1)

